from models.__init__ import CURSOR, CONN

class Manufacturer:

    all = {}

    def __init__(self, name, industry, id = None):
        self.id = id
        self._name = name
        self._industry = industry
        
    def __repr__(self):
        pass

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                'Manufacturer name must be a non-empty string'
            )
    
    @property
    def industry(self):
        return self._industry
    
    @industry.setter
    def industry(self, industry):
        if isinstance(industry, str) and len(industry):
            self._industry = industry
        else:
            raise ValueError(
                'Industry must be a non-empty string'
            )