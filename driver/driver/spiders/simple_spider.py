import scrapy

class oldDriverSpider(scrapy.Spider):
    name = 'elderDriver'
    allowed_domains = ['rosiok.com']
    start_urls=[
        "http://www.rosiok.com/shipin/",
        "http://www.rosiok.com/sishu/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename,'wb') as f:
            f.write(response.body)