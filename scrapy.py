import scrapy
class bestbuy_scarper(scrapy.Spider):
    name = "best_buy"
    urls:list
    urls = [
        'https://www.bestbuy.com/site/searchpage.jsp?st=rtx+2060&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'
    ]

    def parse(self,response):
        for data in response.css('div.shop-sku-list-item'):
            print(f'data:{data}')
            yield
            {
                'name' : data.css('div.sku-title a::attr("text")').get(),
                'url': data.css('div.sku-title a::attr("href")').get(),
             #   'model':data.css('div.variation-info span.sku-value::text').get(),
             #   'price' : data.css('div.priceView-hero-price span::text').get(),
             #   'no_of_reviews':data.css('div.ratings-reviews div.ugc-ratings-reviews span.c-reviews-v4::text').get()
            }
        next_page = response.css('ol.paging-list li.page-item a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page,self.parse)