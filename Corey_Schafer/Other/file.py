#f = open('test.txt', 'r') 'w'=write, 'r' = read
#f.close()

with open('test.txt','r') as f:
    f_contents = f.read()
    for line in f:
        print(line, end ='')
    
    print(f_contents)

with open('test.txt','w') as f:
    f.write('Test')

with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)





