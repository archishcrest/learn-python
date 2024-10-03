import scrapy
from scrapy_splash import SplashRequest
from urllib.parse import urlparse, unquote
from .models import *
import shutil
from scrapy.utils.project import get_project_settings

class DynamicTagSpiderSAP(scrapy.Spider):
    name = 'dynamic_tag_spider_sap'

    custom_settings = {
        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'HTTPCACHE_ENABLED': False,  # Disable Scrapy HTTP cache
        'COOKIES_ENABLED': False,  # Disable cookies
        'DOWNLOAD_DELAY': 0.5,  # Optional: Prevent overwhelming the server
        #'SPLASH_URL': 'http://localhost:8050',  # Adjust if your Splash server is hosted elsewhere
        'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',  # Use Splash-aware dupe filter
        'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage',  # Avoid internal caching
    }

    all_content = []
    site_id = None

    def __init__(self, sitemap_urls=None, site_id=None, tags=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

        # Convert tags to a list if not already one
        if tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['a']  # Default to 'a' tag if no tags are provided

        settings = get_project_settings()
        cache_dir = settings.get('HTTPCACHE_DIR', '.scrapy/httpcache')
        shutil.rmtree(cache_dir, ignore_errors=True)

    def start_requests(self):
        """Override start_requests to use SplashRequest for JavaScript-rendered pages."""
        print(self.sitemap_urls)
        for url in self.sitemap_urls:

            yield SplashRequest(
                url=url, 
                callback=self.parse, 
                args={'wait': 2, 'cache': 0, 'private_mode': True}, 
                headers={'Cache-Control': 'no-cache'}
            )

    def parse(self, response):
        """Main function that parses the specified tags on the page."""
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
                            "content": {
                                "link": link,
                                "text": text
                            }
                        })

                elif tag == 'img':
                    # Handle <img> tags - extract alt text and src (link)
                    alt_text = selector.xpath("@alt").get()
                    link = selector.xpath("@src").get()

                    if link:
                        alt_text = alt_text.strip() if alt_text else "No alt text"
                        self.all_content.append({
                            "tag": "<img>",
                            "content": {
                                "link": link,
                                "alt_text": alt_text
                            }
                        })

                else:
                    # Handle other tags like <p>
                    content = selector.xpath("text()").get()
                    if content:
                        content = content.strip()
                        self.all_content.append({
                            "tag": f"<{tag}>",
                            "content": {
                                "text": content
                            }
                        })

        # Save all content to the database
        SiteContent.objects.create(
            site_id=self.site_id,
            content=self.all_content
        )

    def closed(self, reason):
        """Log the reason when the spider finishes."""
        print(f"Spider closed: {reason}. All data saved.")
