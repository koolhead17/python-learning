def cal_gross_pay(hours_worked, payment_per_hour):
    gross_pay = hours_worked * payment_per_hour
    return gross_pay

name = input("Tell us your name: ")
hour_spent = float(input("Number  hours you worked this week: "))
payment_hour = float(input("Payment made per hour: "))
total_payment = cal_gross_pay(hour_spent, payment_hour)
print('amount paid to ', name, 'for his houly works is $', str(total_payment), sep=' ')

