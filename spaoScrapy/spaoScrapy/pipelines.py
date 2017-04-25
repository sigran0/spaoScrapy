# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from mongoengine import connect
from models.Category import Category
from models.Page import Page
from models.Product import Product
from mongoengine.errors import DoesNotExist

class SpaoscrapyPipeline(object):

    def __init__(self):
        connect('spao', host='localhost', port=27017)

    @classmethod
    def get_uncrawled_category(cls):
        category = None
        try:
            category = Category.objects(is_crawled=False)
        except DoesNotExist as e:
            print 'Does Not Exist'
            return None
        else:
            if len(category) > 0:
                return category[0]
            else:
                return None

    @classmethod
    def get_uncrawled_page(cls):
        page = None
        try:
            page = Page.objects(is_crawled=False)
        except DoesNotExist as e:
            print 'Does Not Exist'
            return None
        else:
            if len(page) > 0:
                return page[0]
            else:
                return None

    @classmethod
    def get_category_by_no(cls, no):
        category = None
        try:
            category = Category.objects(lower_category_no=int(no))
        except DoesNotExist as e:
            print 'Does Not Exist'
            return None
        else:
            if len(category) > 0:
                return category[0]
            else:
                return None

    @classmethod
    def get_page_by_no(cls, no):
        page = None
        try:
            page = Page.objects(goods_no=int(no))
        except DoesNotExist as e:
            print 'Does Not Exist'
            return None
        else:
            if len(page) > 0:
                return page[0]
            else:
                return None

    @classmethod
    def set_crawled_category(cls, category_no):
        try:
            Category.objects(lower_category_no=category_no).update(set__is_crawled=True)
        except DoesNotExist as e:
            print 'Does Not Exist'
            return False
        else:
            return True

    @classmethod
    def set_crawled_page(cls, goods_no):
        try:
            Page.objects(goods_no=goods_no).update(set__is_crawled=True)
        except DoesNotExist as e:
            print 'Does Not Exist'
            return False
        else:
            return True

    @classmethod
    def store_categories(cls, item):
        category = Category(
            top_category=item['top_category'],
            upper_category=item['upper_category'],
            lower_category=item['lower_category'],
            lower_category_no=int(item['lower_category_no'])
        )

        try:
            category.save()
        except Exception as e:
            print e
            return False
        return True

    @classmethod
    def store_page(cls, item):
        page = Page(
            category=item['category'],
            goods_no=item['goods_no'],
            goods_title=item['goods_title'],
            goods_original_price=item['goods_original_price'],
            goods_sale_price=item['goods_sale_price']
        )

        try:
            page.save()
        except Exception as e:
            print e
            return False
        return True

    @classmethod
    def store_product(cls, item):
        product = Product(
            product_code=item['product_code'],
            product_name=item['product_name'],
            product_category=item['product_category'],
            product_color=item['product_color'],
            original_price=item['original_price'],
            discount_price=item['discount_price'],
            product_thumbnail_images=item['product_thumbnail_images'],
            product_url=item['product_url'],
            product_fabric=item['product_fabric'],
            product_gender=item['product_gender']
        )

        try:
            product.save()
        except Exception as e:
            print e
            return False
        return True

    def process_item(self, item, spider):
        return item
