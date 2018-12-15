def net_pay(name, salary):
    print()
    print('Name: ', name)
    print()
    print('Net Pay: ', '$', salary, sep='')


your_name = input("Enter your name: ")
your_salary = float(input("Enter your salary: "))
your_pay_detials = net_pay(your_name,your_salary)

