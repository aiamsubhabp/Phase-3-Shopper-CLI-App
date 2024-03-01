# lib/cli.py
from pyfiglet import Figlet


from helpers import (
    exit_program,
    list_manufacturers,
    find_manufacturer_by_id,
    find_manufacturer_by_name,
    create_manufacturer,
    update_manufacturer,
    delete_manfacturer,
    list_products,
    find_product_by_name,
    find_product_by_id,
    create_product,
    update_product,
    delete_product,
    list_manufacturer_products
)

def greeting():
    print(Figlet(font='chunky').renderText('Shoppers'))

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_manufacturers()
        elif choice == "2":
            find_manufacturer_by_name()
        elif choice == "3":
            find_manufacturer_by_id()
        elif choice == "4":
            create_manufacturer()
        elif choice == "5":
            update_manufacturer()        
        elif choice == "6":
            delete_manfacturer()    
        elif choice == "7":
            list_products()
        elif choice == "8":
            find_product_by_name()
        elif choice == "9":
            find_product_by_id()
        elif choice == "10":
            create_product()
        elif choice == "11":
            update_product()        
        elif choice == "12":
            delete_product() 
        elif choice == "13":
            list_manufacturer_products() 
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all manufacturers")
    print("2. Find manufacturer by name")
    print("3. Find manufacturer by id")
    print("4. Create new manufacturer")
    print("5. Update existing manufacturer")
    print("6. Delete manufacturer")
    print("7. List all products")
    print("8. Find product by name")
    print("9. Find product by id")
    print('10. Create new product')
    print('11. Update existing product')
    print('12. Delete product')
    print('13. List all products by specified manufacturer')




if __name__ == "__main__":
    greeting()
    main()
