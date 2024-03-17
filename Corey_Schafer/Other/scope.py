x = 'global x'
#def test(z):
    #global x #expanding to global scope
    #x = 'local x'
    #print(x)

#test()
#print(x)

def test(z):
    print(z)

test('local z')

def outer():
    x= 'outer x'

    def inner() :
        #nonlocal x
        x = 'inner x'
        print(x) #enclosing
    
    inner()
    print(x)

outer()
print(x)

