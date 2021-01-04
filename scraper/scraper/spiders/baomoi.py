# -*- coding: utf8 -*-
import scrapy

class SohoaVnexpressNet(scrapy.Spider):
    name = "baomoi"

    def start_requests(self):
        urls = [
            'https://baomoi.com/van-hoa.epi',
            'https://baomoi.com/the-gioi.epi',
            'https://baomoi.com/xa-hoi.epi',
            'https://baomoi.com/kinh-te.epi',
            'https://baomoi.com/giao-duc.epi',
            'https://baomoi.com/the-thao.epi',
            'https://baomoi.com/giai-tri.epi',
            'https://baomoi.com/phap-luat.epi'
            'https://baomoi.com/khoa-hoc-cong-nghe.epi',
            'https://baomoi.com/khoa-hoc.epi',
            'https://baomoi.com/doi-song.epi',
            'https://baomoi.com/xe-co.epi',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_artilce)

    def parse_artilce(self, response):
        for entry in response.xpath('//*[@class="story__thumb"]'):
            artilce = {}
            artilce['title'] = entry.xpath('a/img/@alt').get()
            artilce['link'] = entry.xpath('a/@href').extract()[0]
            print(artilce)
