string = input('enter a string and we will do the magic on it: ')
print(string, sep= ' ')
print(string *2, sep= ' ')
print(string *3, sep= ' ')
print(string *4, sep= ' ')


print()
my_String = '@'
for replicator in range(1,11,1):
    string_multipy = my_String * replicator
    print(string_multipy)

print()
# doing reverse of same

my_String1 = '@'
for re_replicator in range(10,1,-1):
    string_multipy1 = my_String1 * re_replicator
    print(string_multipy1)