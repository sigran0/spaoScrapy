#-*- coding: utf-8 -*-

from mongoengine import Document
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import IntField
from mongoengine import ListField
from mongoengine import ObjectIdField


class Page(Document):

    #   Category
    category = ListField(required=True)

    #   Page에서 받아올 수 있는것들
    goods_no = IntField(required=True)
    goods_title = StringField(required=True)
    goods_original_price = IntField(required=True)
    goods_sale_price = IntField(required=True)
    is_crawled = BooleanField(default=False)