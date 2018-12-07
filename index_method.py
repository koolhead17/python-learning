string_1 = 'get some water from the pond'
index_string_1 = string_1.index('water')
print(index_string_1)

# Let us try the exception example
print()

try:
    index_string_1 = string_1.index('cloud')
    print(index_string_1)

except ValueError:
    print('The word you were looking for is not found')
