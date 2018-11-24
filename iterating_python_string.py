welcome = 'hello world'
print(welcome)
print()
for characters in welcome:
    print(characters)


print()

print('another example')

name = 'atul jha'
print(name.upper())
print()
for characters in name:
    ansi_value = ord(characters)
    print('the ansi value of',characters,'is',ansi_value,sep=' ')
