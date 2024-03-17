student = {'name': 'John', 'age' : 25, 'courses' : ['Maht', 'CompSci']}
print(student)
print(student['name'])

#student = {1: 'John', 'age' : 25, 'courses' : ['Maht', 'CompSci']}
#print(student[1])
#print(student['phone'])
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

student['phone'] = '555-5555'
print(student)
student['name'] = 'Jane'
print(student)
student.update({'name' : 'Jane', 'age' : 26, 'phone' : '111-1111'})
print(student)
student = {'name': 'John', 'age' : 25, 'courses' : ['Maht', 'CompSci']}
del student['age']
print(student)
name = student.pop('name')
print(student)
print(name)
student = {'name': 'John', 'age' : 25, 'courses' : ['Maht', 'CompSci']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student :
    print(key)

for key in student.items() :
    print(key)