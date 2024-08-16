'''def my_function():
    return 4


def my_generator():
    yield 4


print(my_function())
print(my_generator())
print(next(my_generator()))'''


'''def my_function():
    my_list=[]
    for x in range (1,5):
        my_list.append(x*10)
    return my_list


def my_generator():
    for x in range (1,5):
        yield x * 10


print(my_function())
print(my_generator())

g= my_generator()

print(next(g))
print(next(g))'''


'''def my_generator():

    x=1
    yield x

    x+=1
    yield x

    x+=1
    yield x


g = my_generator()

print(next(g))
print(next(g))
print(next(g))'''


