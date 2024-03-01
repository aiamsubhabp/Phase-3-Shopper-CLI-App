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
        '''create a new table to persist the attributes of Product instances'''
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

    def save(self):
        '''insert a new row with the name, product title, and manufacturer id values of the current Product object.
        update object id attribute using the primary key value of new row.
        save the object in local dictionary using table row's primary key as dictionary key.'''
        sql = '''
            INSERT INTO products (name, product_type, manufacturer_id)
            VALUES (?, ?, ?)
        '''
        CURSOR.execute(sql, (self.name, self.product_type, self.manufacturer_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        '''updat the table row corresponding to teh current Product instance.'''
        sql = '''
            UPDATE products
            SET name = ?, product_type = ?, manufacturer_id = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.name, self.product_type, self.manufacturer_id, self.id))
        CONN.commit()

    def delete(self):
        '''delete the table row corresponding to the current Product instance, 
        delete the dictionary entry, and reassign id attribute'''
        sql = '''
            DELETE FROM products
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, product_type, manufacturer_id):
        '''initialize a new Product instance and save the object to the database'''
        product = cls(name, product_type, manufacturer_id)
        product.save()
        return product
    
    @classmethod
    def instance_from_db(cls, row):
        '''return a Product object having the attribute values from the table row'''
        product = cls.all.get(row[0])
        if product:
            product.name = row[1]
            product.product_type = row[2]
            product.manufacturer_id = row[3]
        else:
            product = cls(row[1], row[2], row[3])
            product.id = row[0]
            cls.all[product.id] = product
        return product
    
    @classmethod





