# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import collections

class AppannieGameRankPipeline(object):
    def __init__(self):
        self.file = codecs.open('items.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        d1 = collections.OrderedDict()
        d1['date']=item['date']
        d1['rank'] = item['rank']
        d1['free_rank_name']=item['free_rank_name']
        d1['paid_rank_name']=item['paid_rank_name']
        d1['sale_rank_name']=item['sale_rank_name']

        line = json.dumps(d1) + ",\n"
        self.file.write(line.decode('unicode_escape'))
        return item
