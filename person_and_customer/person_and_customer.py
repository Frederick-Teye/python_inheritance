# Write a class named Person with data attributes for a person’s name,
# address, and telephone number.
# Next, write a class named Customer that is a subclass of the Person class.
# The Customer class should have a data attribute for a customer number, and a Boolean
# data attribute indicating whether the customer wishes to be on a mailing list. Demonstrate
# an instance of the Customer class in a simple program.

class Person:
    def __init__(self, name: str, address: str, telephone: str):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def get_name(self):
        return self.__name

    def change_name(self, new_name):
        self.__name = new_name

    def get_address(self):
        return self.__address

    def change_address(self, new_address):
        self.__address = new_address

    def change_telephone(self, new_telephone):
        self.__telephone = new_telephone

    def get_telephone(self):
        return self.__telephone

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Address: {self.__address}\n"
                f"Telephone: {self.__telephone}")


class Customer(Person):
    def __init__(self, name, address, telephone, customer_number: str, mailed_to: bool):
        Person.__init__(self, name, address, telephone)
        self.__customer_number = customer_number
        self.__mailed_to = mailed_to

    def get_number(self):
        return self.__customer_number

    def change_number(self, new_number):
        self.__customer_number = new_number

    def get_mail_to(self):
        return self.__mailed_to

    def change_mail_to(self, mailed_to):
        if mailed_to == "Y":
            self.__mailed_to = True
        elif mailed_to == "N":
            self.__mailed_to = False

    def __str__(self):
        if self.__mailed_to:
            mailed_to = "Yes"
        else:
            mailed_to = "No"
        return (f"{Person.__str__(self)}"
                f"\nCustomer number: {self.__customer_number}"
                f"\nAdded to mail list: {mailed_to}")


