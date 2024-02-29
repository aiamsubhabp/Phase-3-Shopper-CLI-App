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


