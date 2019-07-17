# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundaEachHome(scrapy.Item):
    # define the fields for your item here like:
    home_id = scrapy.Field()
    home_link = scrapy.Field()
    wonen = scrapy.Field()
    kamers = scrapy.Field()
    prijs = scrapy.Field()

class FundaLinkExtractor(scrapy.Item):
    link = scrapy.Field()

class FundaPostCode(scrapy.Item):
    post_code = scrapy.Field()

class FundaEachHomeDesc(scrapy.Item):
    status = scrapy.Field()
    aangeboden_sinds = scrapy.Field()
    bouwjaar = scrapy.Field()
    buitenruimte = scrapy.Field()
    aantal_kamers = scrapy.Field()
    aantal_badkamers = scrapy.Field()
    gelegen_op = scrapy.Field()
    balkon_dakterras = scrapy.Field()
    soort_garage = scrapy.Field()

