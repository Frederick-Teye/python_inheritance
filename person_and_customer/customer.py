import person_and_customer
import pickle
import os

customer_dict = {}
path = "customer.dat"


def main():
    global customer_dict
    if os.path.exists(path):
        with open(path, "rb") as file:
            customer_dict = pickle.load(file)
    else:
        file = open(path, "wb")
        file.close()

    menu()


def menu():
    count = 0
    while True:
        if count == 0:
            user_choice = input("Enter 1 to add new customer"
                                "\nEnter 2 to change customer name"
                                "\nEnter 3 to change customer's address"
                                "\nEnter 4 to change customer's telephone number"
                                "\nEnter 5 to change customer's number"
                                "\nEnter 6 to change customer's mail-to status"
                                "\nEnter 7 to view a customer information"
                                "\nEnter 8 to view all customers information"
                                "\nEnter 9 to delete a customer information"
                                "\nEnter 10 to exit application: ")
            count += 1
        else:
            user_choice = input("\nEnter 1 to add new customer"
                                "\nEnter 2 to change customer name"
                                "\nEnter 3 to change customer's address"
                                "\nEnter 4 to change customer's telephone number"
                                "\nEnter 5 to change customer's number"
                                "\nEnter 6 to change customer's mail-to status"
                                "\nEnter 7 to view a customer information"
                                "\nEnter 8 to view all customers information"
                                "\nEnter 9 to delete a customer information"
                                "\nEnter 10 to exit application: ")
            count += 1

        if user_choice == "1":
            add_new_customer()
        elif user_choice == "2":
            change_customer_name()
        elif user_choice == "3":
            change_customer_address()
        elif user_choice == "4":
            change_customer_phone()
        elif user_choice == "5":
            change_customer_number()
        elif user_choice == "6":
            change_mailto_status()
        elif user_choice == "7":
            view_customer_info()
        elif user_choice == "8":
            view_customers_info()
        elif user_choice == "9":
            delete_customer_info()
        elif user_choice == "10":
            close_app()
            break
        else:
            print("Invalid input..."
                  "\nEnter 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10")


def add_new_customer():
    first_name = get_first_name()
    last_name = get_last_name()
    name = first_name + " " + last_name
    address = input("Enter customer's address: ")
    telephone = input("Enter customer's telephone number: ")
    customer_number = input("Enter customer's number: ")
    mail = input("Do customer want to be mailed to (y/n): ").lower().strip()
    while True:
        if mail == "y" or mail == "n":
            break
        else:
            print("Invalid input...")
            mail = input("Do customer want to be mailed to (y/n): ").lower().strip()
    if mail == "y":
        customer = person_and_customer.Customer(name, address, telephone, customer_number, True)
        customer_dict[name] = customer
    elif mail == 'n':
        customer = person_and_customer.Customer(name, address, telephone, customer_number, False)
        customer_dict[name] = customer
    print("Successfully added a customer...")


def change_customer_name():
    if len(customer_dict) > 0:
        first_name = get_first_name()
        last_name = get_last_name()
        name = first_name + " " + last_name
        if name in customer_dict:
            print("Enter the name you want to change to: ")
            first_name = get_first_name()
            last_name = get_last_name()
            new_name = first_name + " " + last_name
            customer_object = customer_dict.pop(name)
            customer_dict[new_name] = customer_object
            customer_dict[new_name].change_name(new_name)
            print("Name changed successfully...")
        else:
            print("Name do not exist...")
    else:
        print("No customer added yet...")


def change_customer_address():
    if len(customer_dict) > 0:
        first_name = get_first_name()
        last_name = get_last_name()
        name = first_name + " " + last_name
        if name in customer_dict:
            address = input("Enter new address: ")
            customer_dict[name].change_address(address)
            print("Address successfully changed...")
        else:
            print("Name do not exist...")
    else:
        print("No customer added yet...")


def change_customer_phone():
    if len(customer_dict) > 0:
        first_name = get_first_name()
        last_name = get_last_name()
        name = first_name + " " + last_name
        if name in customer_dict:
            telephone = input("Enter new telephone: ")
            customer_dict[name].change_telephone(telephone)
            print("Customer telephone number changed successfully...")
        else:
            print("Name do not exist...")
    else:
        print("No customer added yet...")


def change_customer_number():
    if len(customer_dict) > 0:
        first_name = get_first_name()
        last_name = get_last_name()
        name = first_name + " " + last_name
        if name in customer_dict:
            number = input("Enter new customer number: ")
            customer_dict[name].change_number(number)
            print("Customer number have successfully been changed...")
        else:
            print("Name do not exist...")
    else:
        print("No customer added yet...")


def change_mailto_status():
    if len(customer_dict) > 0:
        first_name = get_first_name()
        last_name = get_last_name()
        name = first_name + " " + last_name
        if name in customer_dict:
            print("Do customer want to be added to our mailing list?")
            mailed_to = input("Enter Y for yes and N for no: ").capitalize().strip()
            while True:
                if mailed_to == "Y" or mailed_to == "N":
                    break
                else:
                    print("Invalid input...")
                    print("Do customer want to be added to our mailing list?")
                    mailed_to = input("Enter Y for yes and N for no: ").capitalize().strip()
            if customer_dict[name].get_mail_to() == True and mailed_to == "Y":
                print("Customer is already part of the mailing list...")
            elif customer_dict[name].get_mail_to() == False and mailed_to == "N":
                print("Customer is already not part of the mailing list...")
            else:
                customer_dict[name].change_mail_to(mailed_to)
                if mailed_to == "Y":
                    print("Customer have successfully been added to mailing list...")
                else:
                    print("Customer have successfully been removed from mailing list...")
    else:
        print("No customer added yet...")


def close_app():
    with open(path, "wb") as file:
        pickle.dump(customer_dict, file)
    print("Goodbye...")


def view_customer_info():
    if len(customer_dict) > 0:
        first_name = get_first_name()
        last_name = get_last_name()
        name = first_name + " " + last_name
        if name in customer_dict:
            print(customer_dict[name])
            print()
        else:
            print("Name do not exist...")
    else:
        print("No customer added yet...")


def view_customers_info():
    if len(customer_dict) > 0:
        print()
        for name in customer_dict:
            print(customer_dict[name])
            print()
    else:
        print("No customer added yet...")


def delete_customer_info():
    first_name = get_first_name()
    last_name = get_last_name()
    name = first_name + " " + last_name
    if name in customer_dict:
        del customer_dict[name]
    else:
        print(name + " do not exist...")


def get_first_name():
    first_name = input("Enter first name: ").strip()
    if first_name != "":
        first_name = first_name[0].upper() + first_name[1:]
        return first_name
    else:
        while True:
            first_name = input("You must enter first name: ").strip()
            if first_name != "":
                return first_name[0].upper() + first_name[1:]


def get_last_name():
    last_name = input("Enter last name: ").strip()
    if last_name != "":
        last_name = last_name[0].upper() + last_name[1:]
        return last_name
    else:
        while True:
            last_name = input("You must enter last name: ").strip()
            if last_name != "":
                return last_name[0].upper() + last_name[1:]


if __name__ == "__main__":
    main()
