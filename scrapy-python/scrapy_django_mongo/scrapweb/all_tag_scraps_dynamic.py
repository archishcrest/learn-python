import sys
# from twisted.internet import asyncioreactor
# asyncioreactor.install()
import scrapy
from urllib.parse import urlparse, unquote
from .models import *

class DynamicTagSpider(scrapy.Spider):
    name = 'dynamic_tag_spider_bak'
    
    custom_settings = {
        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
        #'TWISTED_REACTOR': 'twisted.internet.selectreactor.SelectReactor',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    all_content = []
    site_id = None
    def __init__(self, sitemap_urls=None, site_id = None, tags=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print(f"Processing: ")

        
        self.site_id = site_id

        if sitemap_urls:
            if isinstance(sitemap_urls, str):
                sitemap_urls = [sitemap_urls]
            
            self.sitemap_urls = []
            for url in sitemap_urls:
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                self.sitemap_urls.append(url)

        self.allowed_domains = [urlparse(url).netloc for url in self.sitemap_urls]

        print(f"allowed_domains: {self.allowed_domains}")
        print(f"sitemap_urls: {self.sitemap_urls}")
        print(f"site_id: {site_id}")

        # Convert tags to a list if not already one
        if tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['a']  # Default to 'a' tag if no tags are provided

        # Open the file in 'write' mode to save the output
        # self.file = open('scraped_content.txt', 'w')

    def start_requests(self):
        for url in self.sitemap_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Main function that parses the specified tags on the page."""
        # Print the current URL being processed
        print(f"Processing: {response.url}")

        for tag in self.tags:
            # Select elements based on the current tag
            selectors = response.xpath(f"//{tag}")

            for selector in selectors:
                if tag == 'a':
                    # Handle <a> tags - extract link and text
                    text = selector.xpath("text()").get()
                    link = selector.xpath("@href").get()

                    if link:
                        text = text.strip() if text else "No text"
                        self.all_content.append({
                            "tag": "<a>",
                            "content":{
                                "link":link,
                                "text":text
                            }
                            })
                        #self.file.write(f"Tag: <a>, Text: {text}, URL: {link}\n")

                elif tag == 'img':
                    # Handle <img> tags - extract alt text and src (link)
                    alt_text = selector.xpath("@alt").get()
                    link = selector.xpath("@src").get()

                    if link:
                        alt_text = alt_text.strip() if alt_text else "No alt text"
                        self.all_content.append({
                            "tag": "<img>",
                            "content":{
                                "link":link,
                                "text":alt_text
                            }
                            })
                        #self.file.write(f"Tag: <img>, Alt: {alt_text}, URL: {link}\n")

                else:
                    # Handle <p> tags - extract the text content
                    content = selector.xpath("text()").get()
                    if content:
                        content = content.strip()
                        self.all_content.append({
                            "tag": f"<{tag}>",
                            "content":{
                                "text":content
                            }
                            })
                        #self.file.write(f"Tag: <{tag}>, Content: {content}\n")

                # Add more tags if necessary, using similar logic as above

        SiteContent.objects.create(
            site_id=self.site_id,
            content=self.all_content
            )

    def closed(self, reason):
        """Close the file when the spider finishes."""
        #self.file.close()
        print(f"Spider closed: {reason}. Data saved to 'scraped_content.txt'.")
