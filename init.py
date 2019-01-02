class CurrentAccount:
    def __init__(self,customer_name):
        self.name = customer_name

    def get_customer_name(self):
        return self.name


account_holder = CurrentAccount('Atul Jha')
print('Account holders name is: ', account_holder.get_customer_name(), sep= ' ')



