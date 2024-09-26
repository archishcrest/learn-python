import json
from datetime import datetime
from scrapy.spiders import SitemapSpider
from urllib.parse import urlparse, unquote
from scrapy.exceptions import CloseSpider
import re

# scrapy crawl sitemap_spider_dynamic -a sitemap_urls=https://v2.researchgiant.com/sitemaps/sitemap_index.xml

class FilteredSitemapSpider(SitemapSpider):
    name = "sitemap_spider_dynamic"
    all_filtered_entries = []

    def __init__(self, sitemap_urls=None, *args, **kwargs):
        super(FilteredSitemapSpider, self).__init__(*args, **kwargs)

        if sitemap_urls:
            if isinstance(sitemap_urls, str):
                sitemap_urls = [sitemap_urls]
            
            self.sitemap_urls = []
            for url in sitemap_urls:
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                self.sitemap_urls.append(url)

        self.allowed_domains = [urlparse(url).netloc for url in self.sitemap_urls]

    def sitemap_filter(self, entries):
        for entry in entries:
            yield entry

    def process_sitemap(self, response):

        parsed_url = urlparse(response.url)
        sitemap_name = unquote(parsed_url.path.split("/")[-1].replace(".xml", ""))
        filename = f"{sitemap_name}.txt"

        filtered_entries = list(self.sitemap_filter(self._parse_sitemap(response)))

        url_pattern = r'https?://[^\s<>"]+'

        serializable_entries = []

        for entry in filtered_entries:
            valid_urls = re.findall(url_pattern, str(entry))
            if valid_urls:
                url = valid_urls[0]
                serializable_entries.append({"url": url})

        self.all_filtered_entries.extend(filtered_entries)

        if filtered_entries:
            try:
                with open(filename, 'w') as f:
                    f.write(f"{serializable_entries}\n")
                    #json.dump(filtered_entries, f, indent=4)
                self.log(f'Saved {len(filtered_entries)} entries to {filename}')
            except Exception as e:
                self.log(e)
                raise CloseSpider("No valid entries found, stopping the spider.")

    def _requests_to_follow(self, entries):

        found_sitemap = False
        for entry in entries:
            if entry['loc'].endswith('.xml'):
                found_sitemap = True
                yield self.make_requests_from_url(entry['loc'], callback=self.process_sitemap)
            else:
                yield from super()._requests_to_follow([entry])

        if not found_sitemap:
            self.save_all_entries_to_file()

    def save_all_entries_to_file(self):
        if self.all_filtered_entries:
            filename = "all_filtered_entries.txt"
            with open(filename, 'w') as f:
                f.write(f"{self.all_filtered_entries}\n")
            self.log(f'Saved {len(self.all_filtered_entries)} total entries to {filename}')

    def parse(self, response):
        self.process_sitemap(response)
        self.log("Parse method called, but we are using SitemapSpider's functionality.")

    def closed(self, reason):
        if self.all_filtered_entries:
            self.log(f'Spider closed: {reason}')
            #self.save_all_entries_to_file()
        self.log(f'Spider closed: {reason}')