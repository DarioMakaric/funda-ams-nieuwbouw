from homes_url import HomesUrl
from scrapy.spiders import CrawlSpider
from funda_KHNB_AMS.items import FundaEachHome
from operator import methodcaller

class Funda(CrawlSpider):
    name = "funda_each_home"
    allowed_domains = ["funda.nl"]

    def __init__(self):
        homes_url = HomesUrl()
        self.links = homes_url.homes_url
        self.start_urls = self.links[56:59]

    def parse(self, response):
        item = FundaEachHome()
        for building in response.css(".nieuwbouwproject-woningtypen__type"):
            for home in building.css(".nieuwbouwproject-woningtypen__object"):
                item["home_id"] = home.css(".nieuwbouwproject-woningtypen__object-title a::text").get()
                home_link = home.css(".nieuwbouwproject-woningtypen__object-title a::attr(href)").get()
                item["home_link"] = 'https://www.funda.nl' + home_link
                wonen = home.css(".nieuwbouwproject-woningtypen__object-surface::text").getall()
                item["wonen"] = next(filter(None, map(methodcaller('strip'), wonen)))
                item["kamers"] = home.css(".nieuwbouwproject-woningtypen__object-rooms::text").get()
                item["prijs"] = home.css(".nieuwbouwproject-woningtypen__object-price::text").get()
                yield item

