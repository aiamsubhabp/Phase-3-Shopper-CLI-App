#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.manufacturer import Manufacturer
from models.product import Product

import ipdb

def reset_database():
    Manufacturer.drop_table()
    Product.drop_table()
    Manufacturer.create_table()
    Product.create_table()

    apple = Manufacturer.create('Apple', 'tech')
    toyota = Manufacturer.create('Toyota', 'cars')
    sony = Manufacturer.create('Sony', 'electronics')

    iphone = Product.create('iPhone', 'phone', apple.id)
    tacoma = Product.create('Tacoma', 'truck', toyota.id)


reset_database()
ipdb.set_trace()
