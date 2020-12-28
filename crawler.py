import scrapy
class AmazonSpider(scrapy.Spider):
        name = "amazon"
        start_urls = [
                'https://www.amazon.in/s?k=mobile&ref=nb_sb_noss',
                'https://www.amazon.in/s?k=mobile&page=6&qid=1609099343&ref=sr_pg_7',
                'https://www.amazon.in/s?k=mobile&page=6&qid=1609099343&ref=sr_pg_13',
                'https://www.amazon.in/s?k=mobile&page=6&qid=1609099343&ref=sr_pg_19',
                'https://www.amazon.in/s?k=mobile&page=6&qid=1609099343&ref=sr_pg_25',
        ]

        def parse(self, response):
                for data in response.css('div.s-result-item'):
                        print(data)
                        yield {
                                'name': data.css('span.a-size-medium::text').get(),
                                'discountedPrice': data.css('span.a-price-whole::text').get(),
                                'imgUrl': data.css('div.a-section img.s-image::attr("src")').get(),
                                'actualPrice': data.css('span.a-offscreen::text').get(),
                                'rating': data.css('span.a-icon-alt::text').get(),
                        }
                next_page = response.css('li.a-last a::attr("href")').get()
                if next_page is not None:
                        yield response.follow(next_page, self.parse)