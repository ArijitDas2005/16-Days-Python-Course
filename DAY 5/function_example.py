coffee_prices=[('Cappuccino',1.5),
               ('Espresso',1.2),
               ('Mocha',1.9)]
def most_expensive_coffee(list_of_prices):
    highest_price=0
    my_most_expensive_coffee= ''

    for coffee, price in list_of_prices:
        if price > highest_price:
            highest_price= price
            my_most_expensive_coffee=coffee
        else:
            pass
    return(my_most_expensive_coffee, highest_price)

print(most_expensive_coffee(coffee_prices))