names=['Krishna','Balaram']
age=[18,20]
cities=['Goloka Vrindavan','Vaikuntha']

DHAM=list(zip(names, age, cities))

for names, age, cities in DHAM:
    print(f"{names} is {age} years old, and lives in the {cities} dham.")