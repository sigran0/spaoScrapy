# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from mongoengine import connect
from models.Category import Category
from models.Page import Page
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
        finally:
            if len(category) > 0:
                return category[0]
            else:
                return None

    @classmethod
    def set_crawled_category(cls, category_no):
        try:
            Category.objects(lower_category_no=category_no).update(set__is_crawled=True)
        except DoesNotExist as e:
            print 'Does Not Exist'
            return False
        finally:
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
    def store_page(cls, goods_no):
        page = Page(
            goods_no=int(goods_no)
        )

        try:
            page.save()
        except Exception as e:
            print e
            return False
        return True

    def process_item(self, item, spider):
        return item
