import scrapy

class DynamicTagSpider(scrapy.Spider):
    name = 'dynamic_tag_spider_bak'
    allowed_domains = ['researchgiant.com']
    start_urls = ['https://researchgiant.com/']

    def __init__(self, tags=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Convert tags to a list if not already one
        if tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['a']  # Default to 'a' tag if no tags are provided

        # Open the file in 'write' mode to save the output
        self.file = open('scraped_content.txt', 'w')

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
                        self.file.write(f"Tag: <a>, Text: {text}, URL: {link}\n")

                elif tag == 'img':
                    # Handle <img> tags - extract alt text and src (link)
                    alt_text = selector.xpath("@alt").get()
                    link = selector.xpath("@src").get()

                    if link:
                        alt_text = alt_text.strip() if alt_text else "No alt text"
                        self.file.write(f"Tag: <img>, Alt: {alt_text}, URL: {link}\n")

                else:
                    # Handle <p> tags - extract the text content
                    content = selector.xpath("text()").get()
                    if content:
                        content = content.strip()
                        self.file.write(f"Tag: <{tag}>, Content: {content}\n")

                # Add more tags if necessary, using similar logic as above

    def closed(self, reason):
        """Close the file when the spider finishes."""
        self.file.close()
        print(f"Spider closed: {reason}. Data saved to 'scraped_content.txt'.")
