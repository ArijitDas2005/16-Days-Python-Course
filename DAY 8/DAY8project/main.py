import tickets


def ask():
    print('Welcome to Python Drugstore')

    while True:
        print('[P] - Perfume\n[M] - Medicine\n[C] - Cosmetics')
        try:
            my_product = input('Choose your product: ').upper()
            ['P', 'M', 'C'].index(my_product)
        except ValueError:
            print("That is not valid option")
        else:
            break

    tickets.decorator((my_product))


def start():

    while True:
        ask()
        try:
            another_ticket = input('Do you want another ticket? [Y] [N]').upper()
            ['Y', 'N'].index(another_ticket)
        except ValueError:
            print('Not a valid option')
        else:
            if another_ticket == 'N':
                print('Thanks for visiting our Python Drugstore.')
                break

start()
