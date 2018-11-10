age = int(input("Enter your age: "))

if age >= 18:
    print("Congratulations!! You are eligible to vote. Please collect your card")
    if age == 18:
        print("You are a first time voter, vote with responsibilty.")

else:
    print("Sorry!! You are not eligible to vote yet.")
    if age == 17:
        print("You can come next year and vote.")
