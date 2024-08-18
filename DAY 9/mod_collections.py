'''from collections import Counter

numbers = [1,2,3,4,5,6,7,8,10,3,1,5,6,6,7]
print(Counter(numbers))

print(Counter('Hare Krishna'))

sentence = 'Simple living High Thinking'
print(Counter(sentence.split()))

series = Counter([1,2,3,4,5,6,7,8,6,9,5,3,9])
print(series.most_common())
print(list(series))'''

'''from collections import defaultdict

my_dict = {'one':'green', 'two' : 'blue', 'three' : 'orange'}
print(my_dict['two'])

print('\n')

my_dict1 = defaultdict(lambda: 'Hare Krishna')
my_dict1['one'] = 'green'
print(my_dict1['two'])
print(my_dict1)'''

from collections import namedtuple

my_tuple = (87,34,4)
print(my_tuple[1])

person = namedtuple('person', ['name','height','weight'])
Krishna = person('Krishna',8,70)
print(Krishna.height)
print(Krishna[2])