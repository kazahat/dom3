class Bank:
    def __init__(self,balance = 0):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if self.balance < amount:
            print("Недостаточно средств")
            return self.balance
        else:
            self.balance -= amount
            return self.balance






b = Bank(200)
b.deposit(100)

b.withdraw(50)
b.withdraw(500)
print(b.balance)





