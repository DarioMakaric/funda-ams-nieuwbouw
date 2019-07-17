from homes_url import HomesUrl
from scrapy.spiders import CrawlSpider
from funda_KHNB_AMS.items import FundaEachHomeDesc
from homes_url import EachHomeUrl


class Funda(CrawlSpider):
    name = "funda_home_details"
    allowed_domains = ["funda.nl"]

    def __init__(self):
        home_url = EachHomeUrl()
        self.links = home_url.each_home_url
        self.start_urls = self.links[75:79]

    def parse(self, response):
        item = FundaEachHomeDesc()
        item["aangeboden_sinds"] = response.css("dl:nth-child(2) dd:nth-child(4)::text").get()
        item["status"] = response.css("dl:nth-child(2) dd:nth-child(6)::text").get()
        item["bouwjaar"] = response.css("dl:nth-child(5) dd:nth-child(6)::text").get()
        item["buitenruimte"] = response.css(".object-kenmerken-list dl dd:nth-child(4)::text").get()
        item["aantal_kamers"] = response.css("dl:nth-child(10) dd:nth-child(2)::text").get()
        item["aantal_badkamers"] = response.css("dl:nth-child(10) dd:nth-child(4)::text").get()
        item["gelegen_op"] = response.css("dl:nth-child(10) dd:nth-child(6)::text").get()
        item["balkon_dakterras"] = response.css("dl:nth-child(16) dd::text").get()
        item["soort_garage"] = response.css("dl:nth-child(18) dd::text").get()
        yield item

