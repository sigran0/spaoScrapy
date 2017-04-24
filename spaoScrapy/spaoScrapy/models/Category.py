
from mongoengine import Document
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import IntField


class Category(Document):
    top_category = StringField(required=True)
    upper_category = StringField(required=True)
    lower_category = StringField(required=True)
    lower_category_no = IntField(required=True)
    is_crawled = BooleanField(default=False)
