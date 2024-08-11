my_list=['a','b','c']
my_list2=['d','e','f']
my_list3=my_list+my_list2

my_list3.append('g')
print(my_list3)

deleted=my_list3.pop(0)
print(my_list3)
print(deleted)

my_list3.pop()
print(my_list3)

list=['d','h','a']
list.sort()
list.reverse()
print(list)