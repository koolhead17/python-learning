def default_arguments(msg = 'default', times = 6):
    for i in range(times):
        print(msg)


# using the default argument state.
default_arguments()

print()

#over-riding the defualt argument state
default_arguments('hello', 2)

print()
#over-riding only one argument
default_arguments(times=2)

#over-riding only one argument
print()
default_arguments(msg='It is a great day!')


