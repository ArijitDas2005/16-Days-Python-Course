series = "N-02"

'''if series=="N-01":
    print("Samsung")
elif series=="N-02":
    print("Nokia")
elif series=="N-03":
    print("Motorola")
else:
    print("This pdt. doesn't exist")'''

match series:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("This pdt. doesn't exist")


print("\n")


client={'name':'Hanuman','age':24,'occupation':'Devotee of Lord Rama'}
movie={'title':'KGF2','credits':{'main_star':'Yash','music':'Ravi Basur'}}
items=[client, movie,'book']

for i in items:
    match i:
        case{'name':name,'age':age,'occupation':occupation}:
            print("It is a client")
            print(name,age,occupation)
        case{'title':title,'credits':{'main_star':main_star,'music':music}} :
            print("This is a movie")
            print(title,main_star,music)
        case _:
            print("I don't know what this is")
