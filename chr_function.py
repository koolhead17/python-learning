#The program prints character code for A-Z in capital and small.

for char in range(65,91,1):  # 65 is mqchine value for "A"
    char_value = chr(char)
    print(char, char_value)


print()

# We can simplyfy with range function.

for char in range(65, 65 + 26):
    char_value = chr(char)
    print(char, char_value)



print()

for char in range(97,123,1):  # 97 is machine value for "a"
    char_value = chr(char)
    print(char, char_value)


print()

# We can simplyfy with range function.

for char in range(97, 97 + 26):
    char_value = chr(char)
    print(char, char_value)

