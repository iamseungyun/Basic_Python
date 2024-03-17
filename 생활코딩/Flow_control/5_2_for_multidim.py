persons = [
    ['lee', 'Seoul', 'math'],
    ['tark', 'Masan','eng'],
    ['choo', 'Suwon', 'com']
]

print(persons[0][0])

for person in persons :
    print(person[0]+','+person[2])

person = ['lee', 'Seoul', 'math']

name, address, interest = person
print(name, address, interest)

for name, address, interest in persons :
    print(name, address, interest)