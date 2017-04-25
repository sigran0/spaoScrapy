# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CategoryItem(scrapy.Item):
    top_category = scrapy.Field()
    upper_category = scrapy.Field()
    lower_category = scrapy.Field()
    lower_category_no = scrapy.Field()


class PageItem(scrapy.Item):
    page_number = scrapy.Field()
    now_number = scrapy.Field()
    goods_no = scrapy.Field()
