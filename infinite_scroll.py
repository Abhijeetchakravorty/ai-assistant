import scrapy
class AmazonSpider(scrapy.Spider):
        name = "91mobiles"
        start_urls = [
                'https://www.91mobiles.com/search_page.php?q=laptop&type=all&utm_source=autosuggest'
        ]

        def parse(self, response):
                for data in response.css('div.contentheight1'):
                        print(data)
                        yield {
                                'name': data.css('div.pro_grid_name a:nth-child(1)::attr(href)').extract(),
                        }
                # next_page = response.css('li.a-last a::attr("href")').get()
                # if next_page is not None:
                #         yield response.follow(next_page, self.parse)