import re

text = 'if you need help call in this number (222)-223-2345'

word = 'help' in text
print(word)

pattern = 'pencil'
pattern1 = 'help'
search = re.search(pattern, text)
search1 = re.search(pattern1, text)

# Check if search found a match
if search:
    print(search)
    print(search.span())
    print(search.start())
    print(search.end())
else:
    print("No match found for pattern:", pattern)

# Check if search1 found a match
if search1:
    print(search1)
    print(search1.span())
    print(search1.start())
    print(search1.end())
else:
    print("No match found for pattern:", pattern1)

# Find all matches for pattern
search2 = re.findall(pattern, text)
print(search2)
print(len(search2))

# Iterate over matches for pattern
for finding in re.finditer(pattern, text):
    print(finding.span())



# text = 'call to 234-456-4567 right now'
# pattern = r'\d\d\d-\d\d\d-\d\d\d\d' #or
# pattern1 = r'\d{3}-\d{3}-\d{4}' #or
# pattern2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# result = re.search(pattern, text)
# result1 = re.search(pattern1, text)
# result2 = re.search(pattern2, text)
# print(result)
# print(result1)
# print(result2)
# print(result.group())
# print(result1.group())
# print(result2.group())


# password = input("Password: ")
# pattern = r'D{1}\w{7}'
# check = re.search(pattern, password)
# print(check)




# text = 'Monday and Sunday this store is closed'
#
# search = re.search(r'Monday|Sunday', text)
# search1 = re.search(r'....lose.', text)
# search2 = re.search(r'^\D', text)
# search3 = re.findall(r'[^\s]', text)
# search4 = re.findall(r'[^\s]+', text)
# search5 = re.search(r'^\D$', text)
#
# print(search.group() if search else None)
# print(search1.group() if search1 else None)
# print(search2.group() if search2 else None)
# print(''.join(search3))
# print(' '.join(search4))
# print(search5.group() if search5 else None)
