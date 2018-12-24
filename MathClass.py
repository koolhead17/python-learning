class MathClass():

    def add_them(self,x,y):
        added_value = x + y
        return added_value

    
    def multiply_them(self,x,y):
        multiple_value = x * y
        return multiple_value

    def square_them(self,x,y):
        square_value = x**y
        return square_value



myobject = MathClass()
print(myobject.add_them(3,4))
print(myobject.multiply_them(6,7))
print(myobject.square_them(4,3))



