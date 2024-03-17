from re import L


inform = {'name':'lee', 'address':'Seoul', 'interest':'math'}
print(inform['name'])

for key in inform :
    print(key)

for key in inform :
    print(key, inform[key])

print('======')

informs= [
    {'name':'lee', 'address':'Seoul', 'interest':'math'},
    {'name':'tark', 'address':'Masan', 'interest':'eng'},
    {'name':'choo', 'address':'Suwon', 'interest':'com'}
]

for person in informs :
    print(person)
    print('------')

print('======')

for person in informs :
    for key in person :
        print(key,":",person[key])
    print('----')