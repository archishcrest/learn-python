import scrapy

class LinkCheckerSpider(scrapy.Spider):
    name = 'link_checker'
    allowed_domains = ['v2.researchgiant.com']
    start_urls = ['https://v2.researchgiant.com/']

    # Open the file in 'write' mode when the spider starts
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = open('links_and_texts.txt', 'w')

    def parse(self, response):
        """Main function that parses downloaded pages."""
        # Print the current URL being processed
        print(f"Processing: {response.url}")

        # Get all the <a> tags
        a_selectors = response.xpath("//a")

        # Loop through each <a> tag
        for selector in a_selectors:
            # Extract the link text and href
            text = selector.xpath("text()").get()
            link = selector.xpath("@href").get()

            # Ensure that the link (href) is not None before following it
            if link:
                # Save the link and text to the file
                text = text.strip() if text else "No text"  # Ensure text is not None or empty
                self.file.write(f"Text: {text}, URL: {link}\n")

                # Follow the link to crawl further
                yield response.follow(link, callback=self.parse)
            else:
                # Log when href is missing
                self.log(f"Skipping link with missing href on {response.url}")

    # Close the file when the spider finishes
    def closed(self, reason):
        self.file.close()
        print("Spider closed, file saved.")
