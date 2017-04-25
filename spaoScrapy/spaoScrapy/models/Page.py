
from mongoengine import Document
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import IntField
from mongoengine import ObjectIdField


class Page(Document):
    goods_no = IntField(required=True)
    is_crawled = BooleanField(default=False)