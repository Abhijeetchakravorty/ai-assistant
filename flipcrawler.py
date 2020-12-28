import scrapy
class AmazonSpider(scrapy.Spider):
        name = "amazon"
        start_urls = [
                'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity'
        ]

        def parse(self, response):
                for data in response.css('div._13oc-S'):
                        yield {
                                'name': data.css('a.s1Q9rs::text').get(),
                                'discountedPrice': data.css('div._30jeq3::text').get(),
                                'imgUrl': data.css('img._396cs4::attr("src")').get(),
                                'actualPrice': data.css('div._3I9_wc::text').get(),
                                'rating': data.css('div._3LWZlK::text').get(),
                        }
                next_page = response.css('a._1LKTO3::attr("href")').get()
                if next_page is not None:
                        yield response.follow(next_page, self.parse)