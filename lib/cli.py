# lib/cli.py
from pyfiglet import Figlet


from helpers import (
    exit_program,
    list_manufacturers,
    find_manufacturer_by_id,
    find_manufacturer_by_name,
    create_manufacturer,
    update_manufacturer,
    delete_manfacturer
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
            list_manufacturers()
        elif choice == "3":
            list_manufacturers()
        elif choice == "4":
            list_manufacturers()
        elif choice == "5":
            list_manufacturers()           
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Some useful function")
    print("3. Some useful function")
    print("4. Some useful function")
    print("5. Some useful function")
    print("6. Some useful function")
    print("7. Some useful function")
    print("8. Some useful function")



if __name__ == "__main__":
    greeting()
    main()
