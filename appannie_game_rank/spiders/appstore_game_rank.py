#-*-coding:utf-8-*-
__author__ = 'yodo1'

from scrapy import Spider
from scrapy.http import Request, FormRequest
import json


class apple_game_rank(Spider):
    name = "apple_top100"
    allowed_domains = ["www.appannie.com"]
    download_delay = 1
    start_urls = [
        "https://www.appannie.com/ajax/top-chart/table/?market=ios&country_code=CN&category=6014&date=2017-06-26&rank_sorting_type=rank&page_size=100&order_by=sort_order&order_type=desc&device=iphone"
    ]

    def start_requests(self):
        return [
        Request(
            "https://www.appannie.com/account/login/", meta={'cookiejar': 1},callback=self.post_login)
    ]

    def post_login(self, response):
        csrfmiddlewaretoken=response.xpath('//input[@name="csrfmiddlewaretoken"]/@value').extract_first()
        return FormRequest.from_response(
        response,
        meta={'cookiejar': response.meta['cookiejar']},
        formdata={"csrfmiddlewaretoken":csrfmiddlewaretoken,"next":"/dashboard/home/","username": "appledev@yodo1.com", "password": "Ops20150601"},
        callback=self.after_login,
            dont_filter=True)

    def after_login(self, response):
        for url in self.start_urls:
            yield Request(url,meta={'cookiejar': response.meta['cookiejar']},headers={'x-requested-with':'XMLHttpRequest'})

    def parse(self, response):
        result_json=json.loads(response.text)
        rows=result_json['table']['rows']
        for row in rows:
            rank=row[0]
            free_rank_name=row[1][0]['name']
            paid_rank_name=row[2][0]['name']
            sale_rank_name=row[3][0]['name']
            yield {
                'rank':rank,
                'free_rank_name':free_rank_name,
                'paid_rank_name':paid_rank_name,
                'sale_rank_name':sale_rank_name,
                   }

        # for row in response.xpath('//tr[@class="main-row table-row"]'):
        #     yield {
        #         'rank':row.xpath('td[1]/text()')
        #     }


