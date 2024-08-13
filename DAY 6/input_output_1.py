my_file=open('test.txt')
print(my_file)


print('\n')
my_file=open('test.txt')
print(my_file.read())


print('\n')
my_file=open('test.txt')
print(my_file.readline())


print('\n')
my_file=open('test.txt')
a=my_file.readline()
print(a.upper())


print('\n')
my_file=open('test.txt')

a=my_file.readline()
print(a)
a=my_file.readline()
print(a.rstrip())
a=my_file.readline()
print(a)


print('\n')
my_file=open('test.txt')
for l in my_file:
    print("Here it says: " +l)


print('\n')
my_file=open('test.txt')
all = my_file.readlines()
print(all)
b= all.pop()
print(b)






print('\n')


print(my_file.close())