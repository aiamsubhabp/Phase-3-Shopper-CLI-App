from models.__init__ import CURSOR, CONN

class Manufacturer:

    all = {}

    def __init__(self, name, industry, id = None):
        self.id = id
        self._name = name
        self._industry = industry
