from pathlib import Path

import scrapy


# 1

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     def start_requests(self):
#         urls = [
#             "https://quotes.toscrape.com/page/1/",
#             "https://quotes.toscrape.com/page/2/",
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f"temp_folder/quotes-{page}.html"
#         Path(filename).write_bytes(response.body)
#         self.log(f"Saved file {filename}")




# 2


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         "https://quotes.toscrape.com/page/1/",
#         "https://quotes.toscrape.com/page/2/",
#     ]

#     def parse(self, response):
#         for quote in response.css("div.quote"):
#             yield {
#                 "text": quote.css("span.text::text").get(),
#                 "author": quote.css("small.author::text").get(),
#                 "tags": quote.css("div.tags a.tag::text").getall(),
#             }

# use this comment to run 2
# scrapy crawl quotes -o temp_folder/quotes.json




# 3

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         "https://quotes.toscrape.com/page/1/",
#     ]

#     def parse(self, response):
#         for quote in response.css("div.quote"):
#             yield {
#                 "text": quote.css("span.text::text").get(),
#                 "author": quote.css("small.author::text").get(),
#                 "tags": quote.css("div.tags a.tag::text").getall(),
#             }

#         next_page = response.css("li.next a::attr(href)").get()
#         if next_page is not None:
#             # next_page = response.urljoin(next_page)
#             # yield scrapy.Request(next_page, callback=self.parse)
#             yield response.follow(next_page, callback=self.parse)



# 4


'''
If you pass the tag=humor argument to this spider, you’ll notice that it will only visit URLs from the humor tag, 
such as https://quotes.toscrape.com/tag/humor
'''


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = "https://quotes.toscrape.com/"
        tag = getattr(self, "tag", None)
        if tag is not None:
            url = url + "tag/" + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# use this comment to run 4
# scrapy crawl quotes -O temp_folder/quotes-humor.json -a tag=humor