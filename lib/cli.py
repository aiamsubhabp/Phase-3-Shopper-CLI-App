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
    choice = 0
    while choice == 0:
        start_menu()
        choice = input("> ")
        if choice == "E" or choice == 'e':
            exit_program()
        elif choice == "M" or choice == 'm':
            print('----------------------------------------')
            print('The manufacturers are listed below:\n')
            list_manufacturers()
            print('')
            manufacturer_menu()
        elif choice == "P" or choice == 'p':
            list_products()
        else:
            print("Invalid choice")







        # elif choice == "2":
        #     find_manufacturer_by_name()
        # elif choice == "3":
        #     find_manufacturer_by_id()
        # elif choice == "4":
        #     create_manufacturer()
        # elif choice == "5":
        #     update_manufacturer()        
        # elif choice == "6":
        #     delete_manfacturer()    
        # elif choice == "7":
        #     list_products()
        # elif choice == "8":
        #     find_product_by_name()
        # elif choice == "9":
        #     find_product_by_id()
        # elif choice == "10":
        #     create_product()
        # elif choice == "11":
        #     update_product()        
        # elif choice == "12":
        #     delete_product() 
        # elif choice == "13":
        #     list_manufacturer_products() 
        # else:
        #     print("Invalid choice")

def reroute():
    choice = 0
    while choice == 0:
        print('-----------------------------------------------------------------------')
        print('Type B to go back to the main menu')
        print('Type E to exit')
        choice = input("> ")
        if choice == "E" or choice == 'e':
            exit_program()
        elif choice == 'B' or choice == 'b':
           main()


def start_menu():
    print('-----------------------------------------------------------------------')
    print('\nHello and welcome to Shoppers!')
    print("Please select from one of the following: ")
    print("Type M to see the list of manufacturers")
    print('Type P to see the list of products')
    print("Type E to exit")

def manufacturer_menu():
    choice = 0
    while choice == 0:
        print('-----------------------------------------------------------------------')
        print('Type I to view more information on any manufacturer')
        print('Type C to create a new manufacturer')
        print('Type D to delete a manufacturer')
        print('Type U to update a manufacturer')
        print('Type B to go back to the main menu')
        print('Type E to exit')
        choice = input("> ")
        if choice == "I" or choice == 'i':
            find_manufacturer_by_id()
            reroute()
        elif choice == 'C' or choice == 'c':
            create_manufacturer()
            reroute()
        elif choice == 'I' or choice == 'i':
            find_manufacturer_by_id()
            reroute()
        elif choice == 'D' or choice == 'd':
            delete_manfacturer()
            reroute()
        elif choice == 'U' or choice == 'u':
            update_manufacturer()
            reroute()
        elif choice == 'B' or choice == 'b':
            main()
        elif choice == 'E' or choice == 'e':
            exit_program()


    





    # print("1. List all manufacturers")
    # print("2. Find manufacturer by name")
    # print("3. Find manufacturer by id")
    # print("4. Create new manufacturer")
    # print("5. Update existing manufacturer")
    # print("6. Delete manufacturer")
    # print("7. List all products")
    # print("8. Find product by name")
    # print("9. Find product by id")
    # print('10. Create new product')
    # print('11. Update existing product')
    # print('12. Delete product')
    # print('13. List all products by specified manufacturer')




if __name__ == "__main__":
    greeting()
    main()
