class SavingsAccount:
    minbal = 5000  # Class attribute

    @staticmethod
    def set_minbal(newvalue):
        SavingsAccount.minbal = newvalue

    def __init__(self, acno, customer, balance=0):
        # Object attributes
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.acno} - {self.customer} - {self.balance}"


SavingsAccount.set_minbal(10000)
print (SavingsAccount.minbal)

