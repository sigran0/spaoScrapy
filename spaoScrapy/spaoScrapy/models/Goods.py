
from mongoengine import Document
from mongoengine import StringField
from mongoengine import IntField
from mongoengine import ListField
from mongoengine import DateTimeField

import datetime

class Product(Document):
    product_code = IntField()
    product_name = StringField()
    product_category = ListField()
    product_color = ListField()
    original_price = IntField()
    discount_price = IntField()
    product_thumbnail_images = ListField()
    product_url = StringField()
    product_fabric = StringField()
    product_gender = StringField()
    created_at = DateTimeField(default=datetime.datetime.now)