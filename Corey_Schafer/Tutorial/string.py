# Print welcome message
message = 'Hello world'

print(message)

message_2 = '''Wow
do it!'''

print(message_2)
print(len(message))
print(message[-1])
print(message[0:5])
print(message[:8])

print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('world'))
print(message.find('universe'))

#message = message.replace('world', 'universe')

print(message)

greeting='Hello'
name = 'Michael'

message = greeting + ', ' + name +'. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(help(str))

print(dir(name))