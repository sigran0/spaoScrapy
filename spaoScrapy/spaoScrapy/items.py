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
    category = scrapy.Field()

    goods_no = scrapy.Field()
    goods_title = scrapy.Field()
    goods_original_price = scrapy.Field()
    goods_sale_price = scrapy.Field()


class GoodsItem(scrapy.Item):
    product_code = scrapy.Field()
    product_name = scrapy.Field()
    product_category = scrapy.Field()
    product_color = scrapy.Field()
    original_price = scrapy.Field()
    discount_price = scrapy.Field()
    product_thumbnail_images = scrapy.Field()
    product_url = scrapy.Field()
    product_fabric = scrapy.Field()
    product_gender = scrapy.Field()