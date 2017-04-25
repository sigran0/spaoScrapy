#-*- coding: utf-8 -*-

import scrapy
import re
from ..items import PageItem
from ..pipelines import SpaoscrapyPipeline
from BeautifulSoup import BeautifulSoup

class GoodsSpider(scrapy.Spider):

    name = 'goods'

    start_urls = [
        'http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1610064534'
    ]

    def parse(self, res):
        bs_object = BeautifulSoup(res.body)

        tables = bs_object.find('div', {'id':'data_table01'}).findAll('th')

        """
            Table의 경우 
            http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1610064534 형식과
            http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1608008679 형식이 존재한다.
            내가 파악하지 못한 형태의 table이 있을 경우도 있으므로,
            table을 전체 검색 후 필요한 정보인 색상과 소재를 뽑아내자
        """

        product_fabric = None
        product_color = None

        for table in tables:
            if table.text.find(u"소재") != -1:
                product_fabric = table.findNextSibling('td').text
            if table.text.find(u'색상') != -1:
                product_color = [_str.strip() for _str in table.findNextSibling('td').text.split(',')]
