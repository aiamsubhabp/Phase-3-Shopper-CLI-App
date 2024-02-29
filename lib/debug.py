#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.manufacturer import Manufacturer

import ipdb

Manufacturer.drop_table()
Manufacturer.create_table()

apple = Manufacturer.create('Apple', 'Tech')
print(apple)
apple.delete()
print(apple)

ipdb.set_trace()
