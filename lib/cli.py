# lib/cli.py
from pyfiglet import Figlet

from helpers import (
    exit_program,
    list_manufacturers,
    create_manufacturer,
    update_manufacturer,
    delete_manfacturer,
    create_product,
    delete_product,
    list_manufacturer_products,
    get_product_from_user
)

def greeting():
    print(Figlet(font='chunky').renderText('Shoppers'))

def main():
    while True:
        start_menu()
        choice = input("> ")
        if choice == "E" or choice == 'e':
            exit_program()
        elif choice == "M" or choice == 'm':
            print('-----------------------------------------------------------------------')
            print('')
            manufacturer_menu()
        else:
            print("Invalid menu option. Please select from the menu")

def start_menu():
    print('-----------------------------------------------------------------------')
    print('\nHello and welcome to Shoppers!')
    print("Please select from one of the following: ")
    print("Type M to see the list of manufacturers")
    print("Type E to exit")


def manufacturer_menu():
    while True:
        print('-----------------------------------------------------------------------')
        list_manufacturers()
        print('-----------------------------------------------------------------------')
        print('Type number of manufacturer for more details')
        print('Type C to create a new manufacturer')
        print('Type U to update a manufacturer')
        print('Type D to delete a manufacturer')
        print('Type B to go back to the main menu')
        print('Type E to exit')
        choice = input("> ").lower()
        if choice == "e":
            exit_program()
        elif choice == 'b':
            manufacturer_menu()
        elif choice.isdigit():
            user_choice = int(choice)
            list_manufacturer_products(user_choice)
            print('')
            mfg_action_menu(user_choice)
        elif choice == 'c':
            create_manufacturer()
        elif choice == 'u':
            update_manufacturer()
        elif choice == 'd':
            delete_manfacturer()
        else:
            print("Invalid menu option. Please select from the menu")
            
def mfg_action_menu(user_choice):
    while True:
        print('-----------------------------------------------------------------------')
        print('\nPlease make a selection below')
        print('Type corresponding product number to see more info')
        print('Type A to add a new product')
        print('Type D to delete product')
        print('Type B to go back to the manufacturer menu')
        print('Type E to exit')
        choice = input('> ').lower()
        if choice == 'e':
            exit_program()
        elif choice == 'b':
            manufacturer_menu()
        elif choice.isdigit():
            inner_choice = int(choice)
            get_product_from_user(user_choice, inner_choice)
        elif choice == 'a':
            create_product(user_choice)
            print('-----------------------------------------------------------------------')
            list_manufacturer_products(user_choice)
            print('-----------------------------------------------------------------------')
        elif choice == 'd':
            delete_product(user_choice)
            print('-----------------------------------------------------------------------')
            list_manufacturer_products(user_choice)
            print('-----------------------------------------------------------------------')
        else:
            print("Invalid menu option. Please select from the menu")

if __name__ == "__main__":
    greeting()
    main()
