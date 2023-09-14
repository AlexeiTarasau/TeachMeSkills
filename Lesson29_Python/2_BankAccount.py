class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Top up your account on {amount} rub. New balance: {self.balance}")
        else:
            print("The replenishment amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Removal {amount} rub. New balance: {self.balance}")
        elif amount <= 0:
            print("The replenishment amount must be positive.")
        else:
            print("Insufficient funds in the account.")

account1 = BankAccount("123456789", "Ivanoy Ivan")
account2 = BankAccount("987654321", "Petroy Petr", 1000)

print(f"Account {account1.account_number}, owner: {account1.owner_name}, balance: {account1.balance} rub.")
account1.deposit(500)
account1.withdraw(200)

print(f"Account {account2.account_number}, owner: {account2.owner_name}, balance: {account2.balance} rub.")
account2.withdraw(1500)