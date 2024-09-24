import json
from datetime import datetime
from scrapy.spiders import SitemapSpider
from urllib.parse import urlparse, unquote
from scrapy.exceptions import CloseSpider

import re
# class FilteredSitemapSpider(SitemapSpider):
#     name = "sitemap_spider_static"
#     allowed_domains = ["researchgiant.com"]
#     sitemap_urls = ["https://researchgiant.com/sitemap-index.xml"]
#     filtered_entries = []  # List to store filtered entries

#     def sitemap_filter(self, entries):
#         for entry in entries:
#             date_time = datetime.strptime(entry["lastmod"], "%Y-%m-%d")
#             if date_time.year >= 2005:
#                 self.filtered_entries.append(entry)  # Add to filtered entries list
#                 yield entry

#     def closed(self, reason):
#         # Save the filtered entries to a JSON file once the spider is done
#         with open('./sitemap_scrap/temp_folder/sitemap_spider_static.json', 'w') as f:
#             json.dump(self.filtered_entries, f, indent=4)
#         self.log(f'Saved {len(self.filtered_entries)} entries to filtered_entries.json')


class FilteredSitemapSpider(SitemapSpider):
    name = "sitemap_spider_static_bak"
    allowed_domains = ["v2.researchgiant.com"]
    sitemap_urls = ["https://v2.researchgiant.com/sitemaps/sitemap_index.xml"]

    # Store all filtered entries in a list to save them later
    all_filtered_entries = []

    def sitemap_filter(self, entries):
        # Filter entries with lastmod >= 2005
        for entry in entries:
            
            # Handle the complete datetime format with time and timezone
            # date_time = datetime.strptime(entry["lastmod"], "%Y-%m-%dT%H:%M:%S%z")
            # if date_time.year >= 2005:
            #if isinstance(entry, dict):
                # self.log("sitemap_filter")
                # self.log(entry)
            yield entry

    def process_sitemap(self, response):
        # Generate dynamic filename based on sitemap URL
        parsed_url = urlparse(response.url)
        sitemap_name = unquote(parsed_url.path.split("/")[-1].replace(".xml", ""))
        filename = f"{sitemap_name}.txt"

        self.log(f'entries to {filename}')

        filtered_entries = list(self.sitemap_filter(self._parse_sitemap(response)))

        url_pattern = r'https?://[^\s<>"]+'
        # valid_urls = re.findall(url_pattern, filtered_entries)
        # filtered_entries = valid_urls[0] if valid_urls else None
        #f.write(f"{valid_url}\n")

        serializable_entries = []

        for entry in filtered_entries:
            self.log('--------------------------')
            self.log(str(entry)) 
            self.log('--------------------------')
            valid_urls = re.findall(url_pattern, str(entry))
            if valid_urls:
                url = valid_urls[0]
                serializable_entries.append({"url": url})

        self.log(':::::::::::::::::::::::::::::::')
        self.log(serializable_entries)
        self.log(':::::::::::::::::::::::::::::::')

        

        # Add the filtered entries to the overall list
        self.all_filtered_entries.extend(filtered_entries)

        # Save filtered entries for this specific sitemap
        if filtered_entries:
            try:
                # self.log('filtered_entries to')
                # self.log(filtered_entries)
                # raise CloseSpider("No valid entries found, stopping the spider.")
                with open(filename, 'w') as f:
                    f.write(f"{serializable_entries}\n")
                    #json.dump(filtered_entries, f, indent=4)
                self.log(f'Saved {len(filtered_entries)} entries to {filename}')
            except Exception as e:
                self.log(e)
                raise CloseSpider("No valid entries found, stopping the spider.")

    def _requests_to_follow(self, entries):

        # Override to request nested sitemap files
        found_sitemap = False
        for entry in entries:
            self.log(f'entry::::::::::::::::::::: {entry}')
            # If the entry is a sitemap XML (nested sitemap), request it
            if entry['loc'].endswith('.xml'):
                found_sitemap = True
                yield self.make_requests_from_url(entry['loc'], callback=self.process_sitemap)
            else:
                # Process URLs that are not nested sitemaps (regular URLs)
                yield from super()._requests_to_follow([entry])

        # If no nested sitemap is found, save the current entries to a file
        if not found_sitemap:
            self.save_all_entries_to_file()

    def save_all_entries_to_file(self):
        # Save all filtered entries to a single JSON file if no nested sitemap found
        if self.all_filtered_entries:
            filename = "all_filtered_entries.txt"
            with open(filename, 'w') as f:
                f.write(f"{self.all_filtered_entries}\n")
                #json.dump(self.all_filtered_entries, f, indent=4)
            self.log(f'Saved {len(self.all_filtered_entries)} total entries to {filename}')

    def parse(self, response):
        self.process_sitemap(response)
        # Scrapy requires a parse method, although we're not using it directly
        self.log("Parse method called, but we are using SitemapSpider's functionality.")

    def closed(self, reason):
        # Save entries if the spider is closed and they haven't been saved yet
        if self.all_filtered_entries:
            self.log(f'Spider closed: {reason}')
            #self.save_all_entries_to_file()
        self.log(f'Spider closed: {reason}')