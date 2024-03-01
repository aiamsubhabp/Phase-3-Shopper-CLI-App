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


