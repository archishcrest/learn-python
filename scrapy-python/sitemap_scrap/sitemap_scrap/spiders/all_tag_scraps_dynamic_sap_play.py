import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DynamicTagSpider(scrapy.Spider):
    name = 'dynamic_tag_spider_sap_play'
    allowed_domains = ['v2.researchgiant.com']
    start_urls = ['https://v2.researchgiant.com/']

    def __init__(self, tags=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['a']  # Default to 'a' tag if no tags are provided

        self.file = open('scraped_content_sap.txt', 'w')

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        """Main function that parses the specified tags on the page."""
        print(f"Processing: {response.url}")
        
        # Ensure the Selenium driver is available
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #driver.implicitly_wait(10)
        if driver:
            # Wait for a specific element to load
            self.wait_for_element(driver, 'body')  # Change 'body' to an element that indicates the page has fully loaded

            for tag in self.tags:
                selectors = response.xpath(f"//{tag}")

                print(selectors)

                for selector in selectors:
                    if tag == 'a':
                        text = selector.xpath("text()").get()
                        link = selector.xpath("@href").get()

                        if link:
                            text = text.strip() if text else "No text"
                            self.file.write(f"Tag: <a>, Text: {text}, URL: {link}\n")

                    elif tag == 'img':
                        alt_text = selector.xpath("@alt").get()
                        link = selector.xpath("@src").get()

                        if link:
                            alt_text = alt_text.strip() if alt_text else "No alt text"
                            self.file.write(f"Tag: <img>, Alt: {alt_text}, URL: {link}\n")

                    else:
                        content = selector.xpath("text()").get()
                        if content:
                            content = content.strip()
                            self.file.write(f"Tag: <{tag}>, Content: {content}\n")
        else:
            print('no driver')

    def wait_for_element(self, driver, selector):
        """Wait for a specific element to load on the page."""
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

    def closed(self, reason):
        """Close the file when the spider finishes."""
        self.file.close()
        print(f"Spider closed: {reason}. Data saved to 'scraped_content_sap.txt'.")
