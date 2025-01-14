from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = str(account_number)
        self.balance = float(balance)

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError
        self.balance += float(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError
        self.balance -= float(amount)

    def apply_interest(self):
        self.balance = self.balance*(1+self.interest_rate)

class CheckingAccount(Account):
    def __init__(self, account_number, overdraft_limit):
        super().__init__(account_number)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError
        self.balance += float(amount)

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise InsufficientFundsError
        self.balance -= float(amount)


class InsufficientFundsError(Exception):
    def __init__(self):
        message = "Není dostatek prostředků na účtu."
        super().__init__(message)

class NegativeDepositError(Exception):
    def __init__(self):
        message = "Není možné vložit negativní částku."
        super().__init__(message)


#Vytvoření účtů
savings = SavingsAccount("123456", interest_rate=0.03)
checking = CheckingAccount("654321", overdraft_limit=500)

#Práce s účty
savings.deposit(1000)
savings.apply_interest()

checking.deposit(500)
try:
    checking.withdraw(1200)  # Toto vyvolá výjimku
except InsufficientFundsError as e:
    print(e)

print(savings.get_balance())
print(checking.get_balance())