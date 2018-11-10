age = int(input("Please enter your age: "))

if age > 18:
    print("Your age is " + str(age) + " years, you are eligible to vote.")

elif age == 17:
    print("Your age is " + str(age) + " years, you have to wait for one more year for voting.")

elif age == 18:
    print("Your age is " + str(age) + " years, you are a first time voter. Vote wisely")

else:
    print("Your age is " + str(age) + " years, you are eligible to vote.")

    
    

    
