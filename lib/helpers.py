# lib/helpers.py
from models.manufacturer import Manufacturer
from models.product import Product

def exit_program():
    print("Goodbye!")
    exit()

def list_manufacturers():
    manufacturers = Manufacturer.get_all()
    for i, manufacturer in enumerate(manufacturers, start=1):
        print(i, manufacturer.name)

def get_mfg_id_from_user(user_choice):
    manufacturers = Manufacturer.get_all()
    if 1 <= user_choice <= len(manufacturers):
        # print("this is the id", manufacturers[user_choice - 1].id)
        return manufacturers[user_choice - 1].id
    else:
        return None
    
def get_product_from_user(user_choice):
    products = Product.get_all()
    user_product = products[user_choice-1]
    if 1 <= user_choice <= len(products):
        print('Product Name: ', user_product.name)
        print('Product Type: ', user_product.product_type )

def find_manufacturer_by_name():
    name = input("Enter the manufacturer's name: ")
    manufacturer = Manufacturer.find_by_name(name)
    print(manufacturer) if manufacturer else print(f'{manufacturer} not found')
    

def find_manufacturer_by_id():
    mfg_id = input("Enter the id corresponding to the manufacturer: ")
    manufacturer = Manufacturer.find_by_id(mfg_id)
    print(manufacturer.name, '|', manufacturer.industry) if manufacturer else print(f'Manufacturer {mfg_id} not found\nPlease enter a valid manufacturer id')
    

def create_manufacturer():
    name = input("Enter the manufacturer's name: ")
    industry = input("Enter the manufacturer's industry: ")
    try:
        manufacturer = Manufacturer.create(name, industry)
        print(f'Success: {manufacturer.name} was created!')
    except Exception:
        print('Error creating manufacturer')

def update_manufacturer():
    mfg_id = input("Type the number corresponding to the manufacturer you want to update: ")
    if manufacturer := Manufacturer.find_by_id(mfg_id):
        try:
            name = input("Enter the manufacturers' new name: ")
            manufacturer.name = name
            industry = input("Enter the manufacturer's new industry (if unchanged, enter in the previous industry): ")
            manufacturer.industry = industry

            manufacturer.update()
            print(f'Success {manufacturer.name} was updated!')
        except Exception:
            print("Error updating manufacturer")
    else:
        print(f'Manufacturer id {mfg_id} not found')
        print('Please enter a valid manufacturer id')

def delete_manfacturer():
    mfg_id = input("Enter the number corresponding to the manufacturer you want to delete: ")
    if manufacturer := Manufacturer.find_by_id(mfg_id):
        manufacturer.delete()
        print(f'Manufacturer {manufacturer.name} deleted')
    else:
        print(f'Manufacturer id {mfg_id} not found')
        print("Please enter a valid manufacturer id")

def list_products():
    products = Product.get_all()
    for product in products:
        print(product.id, '|', product.name)

def find_product_by_name():
    name = input("Enter the product's name: ")
    product = Product.find_by_name(name)
    print(product) if product else print(f'{product} not found')

def find_product_by_id():
    product_id = input("Enter the product id: ")
    product = Product.find_by_id(product_id)
    print('Name:', product.name, '| Type:', product.product_type) if product else print(f'Product id {product_id} not found\nPlease enter a valid product id')
    
def create_product(user_choice):
    name = input("Enter the products name: ")
    product_type = input("Enter the product type: ")
    try:
        mfg_id = get_mfg_id_from_user(user_choice)
        manufacturer = Manufacturer.find_by_id(mfg_id)
        if not manufacturer:
            raise Exception('Manufacturer not found')
        product = Product.create(name, product_type, mfg_id)
        print('-----------------------------------------------------------------------')
        print(f'Success, {product.name} was created!')
    except:
        print('Error creating product')

def update_product():
    product_id = input("Enter the product id: ")
    if product := Product.find_by_id(product_id):
        try:
            name = input("Enter the product's new name: ")
            product.name = name
            product_type = input("Enter the product's updated type(if unchanged, enter the previous product type): ")
            product.product_type = product_type
            mfg_id = input("Enter the product's new manufacturer id (if unchanged, enter the previous manufacturer id): ")
            if mfg_id := Manufacturer.find_by_id(mfg_id).id:
                product.manufacturer_id = mfg_id
                product.update()
                print(f'Success: {product.name} was updated!')
        except Exception:
            print("Error upating product")
            print('Please enter a valid manufacturer id')
    else:
        print(f'Product {product_id} not found')

def delete_product(user_choice):
    try: 
        mfg_id = get_mfg_id_from_user(user_choice)
        manufacturer = Manufacturer.find_by_id(mfg_id)

        if not manufacturer:
            raise Exception('Manufacturer not found')
        
        products = manufacturer.products()
        
        product_number = int(input('Enter the number corresponding with the product you want to delete: '))

        if 1 <= product_number <= len(products):
            product = products[product_number-1]
            product.delete()
            print('-----------------------------------------------------------------------')
            print (f'{product.name} was deleted')
        else:
            print('Invalid product number')
    except Exception:
        print('Error deleting song')

def list_manufacturer_products(mfg_number):
    mfg_id = get_mfg_id_from_user(mfg_number)
    manufacturer = Manufacturer.find_by_id(mfg_id)
    if manufacturer:
        products = manufacturer.products()
        if products:
            print(f'Industry: {manufacturer.industry}')
            print(f'{manufacturer.name} Products: ')
            for i, product in enumerate(products, start=1):
                print(i, product.name)
        else:
            print(f"No products found under {manufacturer.name}")
    else:
        print(f'Manufacturer not found. Please select number from list shown')
        


# def list_manufacturer_products():
#     mfg_id = input("Enter the manufacturer id: ")
#     manufacturer = Manufacturer.find_by_id(int(mfg_id))
#     if manufacturer:
#         products = manufacturer.products()
#         if products:
#             print(f'Products manufacturered by {manufacturer.name}: ')
#             for product in products:
#                 print(f'Product id: {product.id}, Name: {product.name}')
#         else:
#             print(f"No products found under {manufacturer.name}")
#     else:
#         print(f'Manufacturer with id: {mfg_id} not found in the database')
# from models.manufacturer import Manufacturer
# from models.product import Product

# # def helper_1():
# #     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()

# def list_manufacturers():
#     manufacturers = Manufacturer.get_all()
#     for i, manufacturer in enumerate(manufacturers, start=1):
#         print(i, manufacturer.name)

# def get_mfg_id_from_user(user_choice):
#     manufacturers = Manufacturer.get_all()
#     if 1 <= user_choice <= len(manufacturers):
#         print("this is the id", manufacturers[user_choice - 1].id)
#         return manufacturers[user_choice - 1].id
#     else:
#         return None

# def find_manufacturer_by_name():
#     name = input("Enter the manufacturer's name: ")
#     manufacturer = Manufacturer.find_by_name(name)
#     print(manufacturer) if manufacturer else print(f'{manufacturer} not found')
    

# def find_manufacturer_by_id():
#     mfg_id = input("Enter the id corresponding to the manufacturer: ")
#     manufacturer = Manufacturer.find_by_id(mfg_id)
#     print(manufacturer.name, '|', manufacturer.industry) if manufacturer else print(f'Manufacturer {mfg_id} not found\nPlease enter a valid manufacturer id')
    

# def create_manufacturer():
#     name = input("Enter the manufacturer's name: ")
#     industry = input("Enter the manufacturer's industry: ")
#     try:
#         manufacturer = Manufacturer.create(name, industry)
#         print(f'Success: {manufacturer.name} was created!')
#     except Exception:
#         print('Error creating manufacturer')

# def update_manufacturer():
#     mfg_id = input("Enter the manufacturer's id: ")
#     if manufacturer := Manufacturer.find_by_id(mfg_id):
#         try:
#             name = input("Enter the manufacturers' new name: ")
#             manufacturer.name = name
#             industry = input("Enter the manufacturer's new industry (if unchanged, enter in the previous industry): ")
#             manufacturer.industry = industry

#             manufacturer.update()
#             print(f'Success {manufacturer.name} was updated!')
#         except Exception:
#             print("Error updating manufacturer")
#     else:
#         print(f'Manufacturer id {mfg_id} not found')
#         print('Please enter a valid manufacturer id')

# def delete_manfacturer():
#     mfg_id = input("Enter the manufacturer's id that you want to delete: ")
#     if manufacturer := Manufacturer.find_by_id(mfg_id):
#         manufacturer.delete()
#         print(f'Manufacturer {manufacturer.name} deleted')
#     else:
#         print(f'Manufacturer id {mfg_id} not found')
#         print("Please enter a valid manufacturer id")

# def list_products():
#     products = Product.get_all()
#     for product in products:
#         print(product.id, '|', product.name)

# def find_product_by_name():
#     name = input("Enter the product's name: ")
#     product = Product.find_by_name(name)
#     print(product) if product else print(f'{product} not found')

# def find_product_by_id():
#     product_id = input("Enter the product id: ")
#     product = Product.find_by_id(product_id)
#     print('Name:', product.name, '| Type:', product.product_type) if product else print(f'Product id {product_id} not found\nPlease enter a valid product id')
    
# def create_product():
#     name = input("Enter the products name: ")
#     product_type = input("Enter the product type: ")
#     mfg_id = input("Enter the product's manufacturer id: ")
#     try:
#         if mfg_id := Manufacturer.find_by_id(mfg_id).id:
#             product = Product.create(name, product_type, mfg_id)
#             print(f'Success: {product.name} was created!')
#         else:
#             print(f'Manufacturer id {mfg_id} not found. Please select an existing manufacturer id')
#     except Exception:
#         print("Error creating product:", name)

# def update_product():
#     product_id = input("Enter the product id: ")
#     if product := Product.find_by_id(product_id):
#         try:
#             name = input("Enter the product's new name: ")
#             product.name = name
#             product_type = input("Enter the product's updated type(if unchanged, enter the previous product type): ")
#             product.product_type = product_type
#             mfg_id = input("Enter the product's new manufacturer id (if unchanged, enter the previous manufacturer id): ")
#             if mfg_id := Manufacturer.find_by_id(mfg_id).id:
#                 product.manufacturer_id = mfg_id
#                 product.update()
#                 print(f'Success: {product.name} was updated!')
#         except Exception:
#             print("Error upating product")
#             print('Please enter a valid manufacturer id')
#     else:
#         print(f'Product {product_id} not found')

# def delete_product():
#     product_id = input("Enter the product id: ")
#     if product := Product.find_by_id(product_id):
#         product.delete()
#         print(f'{product.name} was deleted')
#     else:
#         print(f'Product id {product_id} not found')

# def list_manufacturer_products(mfg_number):
#     mfg_id = get_mfg_id_from_user(mfg_number)
#     manufacturer = Manufacturer.find_by_id(mfg_id)
#     if manufacturer:
#         products = manufacturer.products()
#         if products:
#             print(f'Products manufacturered by {manufacturer.name}: ')
#             for i, product in enumerate(products, start=1):
#                 print(i, product.name)
#         else:
#             print(f"No products found under {manufacturer.name}")
#     else:
#         print(f'Manufacturer with id: {mfg_id} not found in the database')
