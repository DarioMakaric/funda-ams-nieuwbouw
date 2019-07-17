
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from funda_KHNB_AMS.items import FundaLinkExtractor


class Funda(CrawlSpider):
    name = "funda_link_extractor"
    allowed_domains = ["funda.nl"]

    def __init__(self):
        self.start_urls = ["https://www.funda.nl/nieuwbouw/amsterdam/p%s/" % page for page in range(1, 5)]
        self.base_url = "https://www.funda.nl/nieuwbouw/amsterdam/project-"
        self.le = LinkExtractor(allow=r'%s\d{8}.*/' % self.base_url)

    def parse(self, response):
        item = FundaLinkExtractor()
        links = self.le.extract_links(response)
        for link in links:
            item["link"] = link.url
            yield item

