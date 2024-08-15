class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Client(Person):

    def __init__(self, first_name, last_name, account_number, balance=0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'Client: {self.first_name} {self.last_name}\nAccount Balance {self.account_number}: ${self.balance}'

    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        print('Deposit accepted')

    def withdraw(self, amount_withdraw):
        if self.balance >= amount_withdraw:
            self.balance -= amount_withdraw
            print('Withdraw done')
        else:
            print('Insufficient funds')


def create_client():
    first_name_ct = input("Enter your name: ")
    last_name_ct = input("Your last name: ")
    account_number = input("Enter your account number: ")
    client1 = Client(first_name_ct, last_name_ct, account_number)

    return client1


def start():
    my_customer = create_client()
    print(my_customer)
    option = 0

    while option != 'E':
        print("Choose: Deposit (D), Withdraw (W), or Exit (E)")
        option = input()

        if option == 'D':
            dep_amount = int(input("Deposit amount: "))
            my_customer.deposit(dep_amount)
        elif option == 'W':
            with_amount = int(input("Withdraw amount: "))
            my_customer.withdraw(with_amount)

        print(my_customer)

    print("Thank you for using Python Bank")

start()
