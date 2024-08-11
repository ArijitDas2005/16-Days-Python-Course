#inside can be any brackets () ir [] or {}
my_set= set((1,2,3,4,5))
print(my_set)
print(type(my_set))

#OR
other_set= {1,2,3,4,5}
print(other_set)
print(type(other_set))

s1={1,2,3}
s1.add(4)
print(s1)

s1.remove(1)
print(s1)

s2={4,5,6}
s3=s1.union(s2)
print(s3)

s3.discard(2)
print(s3)

s3.pop()
print(s3)

s3.clear()
print(s3)
