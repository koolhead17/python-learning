class BankAccount:
    def __init__(self, accounholder_name, accountholder_age):
        self.name = accounholder_name
        self.age = accountholder_age

    def get_accounholder_name(self):
        return self.name

    def get_accounholder_age(self):
        return self.age    

my_bankaccount = BankAccount("Atul Jha", "33")
print("my name is: ", my_bankaccount.get_accounholder_name(), ', my age is:', my_bankaccount.get_accounholder_age(), " years", sep=" ")
