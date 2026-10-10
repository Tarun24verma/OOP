from dataclasses import dataclass

class BankAccount:
    bank_name="PyBank"

    def __init__(self,owner, balance=0):
        self.owner=owner
        self._account_type="savings"
        self.__balance=0
        self.balance=balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
class SavingsAccount(BankAccount):
    def info(self):
        return f"{self.owner}'s {self._account_type} account"

@dataclass
class Address:
    city: str
    pincode: str

class Customer:
    def __init__(self, name, city, pincode, opening_balance):
        self.name = name
        self.address = Address(city, pincode)
        self.account = BankAccount(name, opening_balance)

acc = BankAccount("Asha", 1000)
print(acc.owner)
print(acc._account_type)
print(acc._BankAccount__balance)

print(acc.balance)
acc.deposit(500)
print(acc.balance)

try:
    acc.balance=-50
except ValueError as e:
    print("Error", e)

print(SavingsAccount("Ravi").info())

c=Customer("Meera", "jaipur", "302001", 2000)
print(c.address)
print(c.account.balance)