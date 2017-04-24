#-*- coding: utf-8 -*-

import scrapy
from ..items import CategoryItem
from ..pipelines import SpaoscrapyPipeline


class CategorySpider(scrapy.Spider):

    name = "category"

    start_urls = [
        'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1607300073',   #   Men
        'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1607300075',   #   Women
        'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1607300070',   #   Acc
    ]

    def parse(self, res):
        top_category_title = res.css('div.title > h2.tit_h2::text').extract()[0]
        upper_categories = res.css('div.lnb_cate01 > ul > li')

        for upper_category in upper_categories:
            upper_category_title = upper_category.xpath('@data-ga-tag').extract()[0][9:]
            lower_categories = res.css('div.depth2 > ul > li')

            for lower_category in lower_categories:
                lower_category_title = lower_category.xpath('@data-ga-tag').extract()[0][9:]
                lower_category_no = lower_category.css('li > a').xpath('@onclick').re('[0-9]+')[0]

                item = CategoryItem()
                item['top_category'] = top_category_title
                item['upper_category'] = upper_category_title
                item['lower_category'] = lower_category_title
                item['lower_category_no'] = lower_category_no

                pipeline = SpaoscrapyPipeline()
                result = pipeline.store_categories(item, self)
                
                if result is not True:  #   저장시 문제가 생긴경우
                    print 'Store Error!'
                    yield None

                yield item
