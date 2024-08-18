import re

'''text = 'if you need help call in this number (222)-223-2345'

#word = 'help' in text
#print(word)

#pattern = 'pencil'
pattern = 'help'
search = re.search(pattern, text)
print(search)
print(search.span())
print(search.start())
print(search.end())

search1 = re.findall(pattern, text)
print(search1)
print(len(search1))

for finding in re.finditer(pattern, text):
    print(finding.span())'''


'''text = 'call to 234-456-4567 right now'
#pattern = r'\d\d\d-\d\d\d-\d\d\d\d' or
#pattern = r'\d{3}-\d{3}-\d{4}' or
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(pattern, text)
print(result)
print(result.group())'''


'''password = input("Password: ")
pattern = r'D{1}\w{7}'
check = re.search(pattern, password)
print(check)'''


text = 'Monday and Sunday this store is closed'
#search = re.search(r'Monday|Sunday', text)
#search = re.search(r'....lose.',text)
#search = re.search(r'^\D',text)
#search = re.findall(r'[^\s]',text)
search = re.findall(r'[^\s]+',text)
#search = re.search(r'^\D$',text)
print(search)
print(''.join(search))