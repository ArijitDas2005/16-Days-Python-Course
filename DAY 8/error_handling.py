'''def addition():
    n1=int(input("The first number: "))
    n2=int(input("The second number: "))
    print(n1+n2)
    print("Thanks for adding"+ n1)


try:
    #The code you want to check
    addition()

except:
    #Execute if there is an error
    print("Something is wrong here")

else:
    #Code that will be executed if there is no error
    print("You did great")

finally:
    #The code will be executed anyway
    print("That's all")'''




'''def addition():
    n1=int(input("The first number: "))
    n2=int(input("The second number: "))
    print(n1+n2)
    print("Thanks for adding"+ n1)


try:
    #The code you want to check
    addition()

except TypeError:
    #Execute if there is an error
    print("Something is wrong here")

except ValueError:
    print("This is not a number")

else:
    #Code that will be executed if there is no error
    print("You did great")

finally:
    #The code will be executed anyway
    print("That's all")'''




def ask_number():

    while True:

        try:
            number = int(input("Enter a number: "))

        except:
            print("That is not a number")

        else:
            print(f"You have entered number {number}")
            break

    print("Thank You")


ask_number()


