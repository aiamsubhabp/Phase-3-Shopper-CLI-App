# lib/helpers.py
from models.manufacturer import Manufacturer
from models.product import Product

# def helper_1():
#     print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_manufacturers():
    manufacturers = Manufacturer.get_all()
    for manufacturer in manufacturers:
        print (manufacturer)

def find_manufacturer_by_name():
    name = input("Enter the manufacturer's name: ")
    manufacturer = Manufacturer.find_by_name(name)
    print(manufacturer) if manufacturer else print(f'{manufacturer} not found')

def find_manufacturer_by_id():
    mfg_id = input("Enter the manufacturer's id: ")
    manufacturer = Manufacturer.find_by_id(mfg_id)
    print(manufacturer) if manufacturer else print(f'Manufacturer {mfg_id} not found')

def create_manufacturer():
    name = input("Enter the manufacturer's name: ")
    industry = input("Enter the manufacturer's industry: ")
    try:
        manufacturer = Manufacturer.create(name, industry)
        print(f'Success: {manufacturer}')
    except Exception as exc:
        print('Error creating manufacturer: ', exc)

def update_manufacturer():
    mfg_id = input("Enter the manufacturer's id: ")
    if manufacturer := Manufacturer.find_by_id(mfg_id):
        try:
            name = input("Enter the manufacturers' new name: ")
            manufacturer.name = name
            industry = input("Enter the manufacturer's new industry (if unchanged, enter in the previous industry): ")
            manufacturer.industry = industry

            manufacturer.update()
            print(f'Success {manufacturer}')
        except Exception as exc:
            print("Error updating manufacturer: ", exc)
        else:
            print(f'Manufacturer {mfg_id} not found')

def delete_manfacturer():
    mfg_id = input("Enter the manufacturer's id: ")
    if manufacturer := Manufacturer.find_by_id(mfg_id):
        manufacturer.delete()
        print(f'Manufacturer {mfg_id} deleted')
    else:
        print(f'Manufacturer {mfg_id} not found')

def list_products():
    products = Product.get_all()
    for product in products:
        print(product)

def find_product_by_name():
    name = input("Enter the product's name: ")
    product = Product.find_by_name(name)
    print(product) if product else print(f'{product} not found')

def find_product_by_id():
    product_id = input("Enter the product id: ")
    product = Product.find_by_id(product_id)
    print(product) if product else print(f'Product {product_id} not found')

def create_product():
    name = input("Enter the products name: ")
    product_type = input("Enter the product type: ")
    mfg_id = input("Enter the product's manufacturer id: ")
    try:
        if mfg_id := Manufacturer.find_by_id(mfg_id).id:
            product = Product.create(name, product_type, mfg_id)
            print(f'Success: {product}')
        else:
            print(f'Manufacturer id not found')
    except Exception as exc:
        print("Error creating product: ", exc)

def update_product():
    product_id = input("Enter the product id: ")
    if product := Product.find_by_id(product_id):
        try:
            name = input("Enter the product's new name: ")
            product.name = name
            product_type = input("Enter the product's updated type(if unchanged, enter the previous product type)")
            product.product_type = product_type
            mfg_id = input("Enter the product's new manufacturer id (if unchanged, enter the previous manufacturer id)")
            if mfg_id := Manufacturer.find_by_id(mfg_id).id:
                product.manufacturer_id = mfg_id
                product.update()
                print(f'Success: {product}')
        except Exception as exc:
            print("Error upating product: ", exc)
    else:
        print(f'Product {product_id} not found')

def delete_product():
    product_id = input("Enter the product id: ")
    if product := Product.find_by_id(product_id):
        product.delete()
        print(f'Product {product_id} deleted')
    else:
        print(f'Product {product_id} not found')

def list_manufacturer_products():
    mfg_id = input("Enter the manufacturer id: ")
    manufacturer = Manufacturer.find_by_id(int(mfg_id))
    if manufacturer:
        products = manufacturer.products()
        if products:
            print(f'Products manufacturered by {manufacturer.name}: ')
            for product in products:
                print(f'Product id: {product.id}, Name: {product.name}')
        else:
            print(f"No products found under {manufacturer.name}")
    else:
        print(f'Manufacturer with id: {mfg_id} not found in the database')


