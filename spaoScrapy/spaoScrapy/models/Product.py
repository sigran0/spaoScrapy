#-*- coding: utf-8 -*-

from mongoengine import Document
from mongoengine import StringField
from mongoengine import IntField
from mongoengine import ListField
from mongoengine import DateTimeField

import datetime

"""
    구현 해야할것
    product_color
    product_thumbnail_images
    product_fabric
    product_gender
"""

class Product(Document):
    product_code = IntField()               #   O
    product_name = StringField()            #   O
    product_category = ListField()          #   O
    product_color = ListField()             #   O
    original_price = IntField()             #   O
    discount_price = IntField()             #   O
    product_thumbnail_images = ListField()  #   O
    product_url = StringField()             #   O
    product_fabric = StringField()          #   O
    product_gender = StringField()          #   X
    created_at = DateTimeField(default=datetime.datetime.now)