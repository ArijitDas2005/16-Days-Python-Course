my_list=['a','b','c']
for letter in my_list:
    #print(letter)
    letter_number= my_list.index(letter) + 1
    print(f"letter {letter_number}: {letter}")

print("\n")

numbers=[1,2,3,4,5]
my_value= 0
for number in numbers:
    my_value =  my_value + number
    print(my_value)
print(my_value)
