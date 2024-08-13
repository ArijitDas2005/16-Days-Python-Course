from random import shuffle

#initial list
sticks=['-','--','---','----']

#mixing sticks
def mix(my_list):
    shuffle(my_list)
    return(my_list)

#choose number
def try_your_luck():
    a_try= ' '
    while a_try not in ['1','2','3','4']:
        a_try=input("Choose a number: ")
    return int(a_try)

#check players try
def verify_try(a_list, a_try):
    if a_list[a_try-1]=='-':
        print("Wash the dishes")
    else:
        print("This time you are safe")

    print(f'You got {a_list[a_try-1]}')

mixed_sticks= mix(sticks)
selection= try_your_luck()
verify_try(mixed_sticks, selection)