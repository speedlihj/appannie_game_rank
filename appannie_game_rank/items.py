# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppannieGameRankItem(scrapy.Item):
    rank=scrapy.Field()
    free_rank_name=scrapy.Field()
    paid_rank_name=scrapy.Field()
    sale_rank_name=scrapy.Field()
