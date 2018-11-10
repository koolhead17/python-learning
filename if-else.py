bank_charge = 5
bank_bonus = 1
account_balance = -50

if account_balance < 0:
    account_balance = account_balance - bank_charge

else:
    account_balance = account_balance + bank_bonus

print("Your account balance at present moment is: " + str(account_balance))    
