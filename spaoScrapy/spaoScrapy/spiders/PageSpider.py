#-*- coding: utf-8 -*-

import scrapy
import re
from ..items import PageItem
from ..pipelines import SpaoscrapyPipeline
from BeautifulSoup import BeautifulSoup

class PageSpider(scrapy.Spider):

    name = 'page'
    url = ''

    start_urls = [
        'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1704316476&pageSize=1000&listOnly=Y&color_info='
    ]

    def parse(self, res):

        pipeline = SpaoscrapyPipeline()

        #   Category Number를 regex로 찾아오기
        category_num = re.findall(r'[0-9]{6,15}', res.url)[0]

        bs_object = BeautifulSoup(res.body)

        #   아이템이 있는지 없는지부터 판별한다.
        item_exist = bs_object.find('div', {'class':'no_data_txt'})

        if item_exist is None:
            lists = bs_object.find(id='goodsList').findAll('ul', {'class': 'list'})

            for list in lists:

                products = list.findAll('li')

                for product in products:

                    onclick = product.find('a', recursive=False)['onclick']
                    goods_no = re.findall(r'goods_no:\'[0-9]+', onclick)[0][10:]

                    pipeline.store_page(goods_no)

        pipeline.set_crawled_category(category_num)
        next_category = pipeline.get_uncrawled_category()

        if next_category is not None:
            next_category_no = next_category['lower_category_no']
            url = 'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=%d&pageSize=1000&listOnly=Y&color_info=' %(next_category_no)

            request = scrapy.Request(url=url)
            yield request