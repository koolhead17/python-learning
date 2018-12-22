class DemoClass:
    """ This is a Demo Class docmumentation box. """
    pass   

my_instance = DemoClass()

print(type(my_instance))
print(id(my_instance))
print(DemoClass.__doc__)
print()
print(my_instance.__doc__)
print()

print(dir(DemoClass))




