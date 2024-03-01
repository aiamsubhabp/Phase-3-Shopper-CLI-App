from models.__init__ import CURSOR, CONN
from models.manufacturer import Manufacturer

class Product:

    all = {}

    def __init__(self, name, product_type, manufacturer_id, id = None):
        self.id = id
        self.name = name
        self.product_type = product_type
        self.manufacturer_id = manufacturer_id
    
    def __repr__(self):
        return (
            f"<Product {self.id}: {self.name}, {self.product_type}, " + 
            f"Manufacturer ID: {self.manufacturer_id}>"
        )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                'Name must be a non-empty string'
            )
    
    @property
    def product_type(self):
        return self._product_type
    
    @product_type.setter
    def product_type(self, product_type):
        if isinstance(product_type, str) and len(product_type):
            self._product_type = product_type
        else:
            raise ValueError(
                'Product type must be a non-empty string'
            )
    
    @property
    def manufacturer_id(self):
        return self._manufacturer_id
    
    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        if isinstance(manufacturer_id, int) and Manufacturer.find_by_id(manufacturer_id):
            self._manufacturer_id = manufacturer_id
        else:
            raise ValueError(
                'manufacturer id must reference a manufacturer in the database'
            )
        
    @classmethod
    def create_table(cls):
        '''create a mew table to persist the attributes of Product instances'''
        sql = '''
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            product_type TEXT,
            manufacturer_id INTEGER,
            FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id))
        '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        '''drop the table that persists Product instances'''
        sql = '''
            DROP TABLE IF EXISTS products;
        '''
        CURSOR.execute(sql)
        CONN.commit()

        


