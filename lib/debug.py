#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.manufacturer import Manufacturer

import ipdb

def reset_database():
    Manufacturer.drop_table()
    Manufacturer.create_table()

    apple = Manufacturer.create('Apple', 'tech')
    toyota = Manufacturer.create('Toyota', 'cars')
    sony = Manufacturer.create('Sony', 'electronics')

reset_database()
ipdb.set_trace()
