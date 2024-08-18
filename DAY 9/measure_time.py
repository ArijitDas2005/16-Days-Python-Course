'''import time


def for_test(number):
    my_list = []
    for num in range(1, number + 1):
        my_list.append(num)
    return my_list


def while_test(number):
    my_list = []
    counter = 1
    while counter <= number:
        my_list.append(counter)
        counter +=1
    return my_list


beginning = time.time()
for_test(10000)
ending = time.time()
print(ending - beginning)

beginning = time.time()
while_test(10000)
ending = time.time()
print(ending - beginning)'''


import timeit

declaration = '''
for_test(10)
'''

my_setup = '''
def for_test(number):
    my_list = []
    for num in range(1, number + 1):
        my_list.append(num)
    return my_list
'''

length = timeit.timeit(declaration, my_setup, number= 100000)
print(length)

declaration2 = '''
while_test(10)
'''

my_setup2 = '''
def while_test(number):
    my_list = []
    counter = 1
    while counter <= number:
        my_list.append(counter)
        counter +=1
    return my_list
'''

length2 = timeit.timeit(declaration2, my_setup2, number= 100000)
print(length2)
