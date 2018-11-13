name = input("Please provide us your name: ")
marks = int(input("Provide us your marks awarded: "))
if marks >= 70:
    awarded = "Distiction"
elif marks >= 60:
    awarded = "First Division"
elif marks >= 50:
    awarded = "Pass"
elif marks >= 40:
    awarded = "Just Pass"
else:
    awarded: "Fail"                

print("hello " +str(name)+", you have secured " +str(marks)+" marks. You are awarded with " + str(awarded)+ ".")
