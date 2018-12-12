def area(lenght, breadth):
    the_area = lenght * breadth
    return the_area


the_length = float(input('Enter the lenght: '))
the_breadth = float(input('Enter the breadth: '))
our_area = area(the_length, the_breadth)
print('The area of rectangle is ', our_area, sep= ' ')


