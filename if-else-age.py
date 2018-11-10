age = int(input("Please tell us your age: "))

if age > 18:
    print("Please collect your voting card. You are eligible to vote.")

elif age == 18:
    print("Congratulations, you are a first time voter. Choose your representatives wisely.")

else:
    print("You are too young to vote")
