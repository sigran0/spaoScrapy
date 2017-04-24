# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from mongoengine import connect
from models.Category import Category


class SpaoscrapyPipeline(object):

    def __init__(self):
        connect('spao', host='localhost', port=27017)

    def store_categories(self, item, spider):
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

    def process_item(self, item, spider):
        return item
