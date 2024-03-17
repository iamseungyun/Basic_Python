if True :
    print('Conditional was True')

if False :
    print('Conditional was True') 

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else :
    print('No match')

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in :
    print('Admin page')
else :
    print('Bad Creds')

if user == 'Admin' or logged_in :
    print('Admin page')
else :
    print('Bad Creds')

if not logged_in :
    print('Please Log In')
else :
    print('Welcome')

a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)
print(id(a))
print(id(b))

a = [1,2,3]
b = a
print(a==b)
print(a is b)
print(id(a))
print(id(b))

# False values :
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. ex) '', (), []
    # Any empty mapping. ex) {}

condition = 0
if condition :
    print('Conditional was True')
else :
    print('Conditional was False') 

condition = 10
if condition :
    print('Conditional was True')
else :
    print('Conditional was False') 