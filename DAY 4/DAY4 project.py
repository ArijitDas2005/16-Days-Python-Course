from random import randint

guess=0
secret_number= randint(1,100)
estimation=0
name= input("Username:")

print(f"OK {name}, I have thought of a number between 1 and 100\n You have 8 guesses to guess")

while guess<8:
    estimation=int(input("What is the number: "))
    guess+=1

    if estimation<secret_number:
        print("My number is lower")
    elif estimation>secret_number:
        print("My number is higer")
    else:
        print(f"Congratulations {name}! You have guessed in {guess} attempts")
        break

if estimation!=secret_number:
    print(f"Sorry {name}, you have run out of attempts\n BETTER LUCK NEXT TIME")

