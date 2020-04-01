# Bank account examples (with data) using decimal instead of floating
# point numbers
from decimal import *

class Account(object):
    """ This class represents a bank account 
    Constants:
        qb: Decimal formatting for bankers rounding

    Attributes:
        name (str): The name of the bank account
        balance (float): The current acount balance in dollars

    Methods:
        deposit: Checks if amount provided as argument is above 0, if true
            then amount is added to the the account instance's balance
            attribute and the amount is returned.
        withdraw: Checks if amount provided as argument is above 0 and above
            the account instance's balance attribute. If true, the account
            instance's balance attribute is reduced by the amount and the
            amount is returned. If false, a statement is printed notifying the
            user of the withdraw parameters and 0.0 is returned.
        show_balance: Prints the account instance's current name and balance.
    """
    # class constant accesible without creating an instance
    _qb = Decimal('0.00') 

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = Decimal(opening_balance).quantize(Account._qb)
        print("Account created for {}".format(name), end='')
        self.show_balance()

    # hint that method takes float type
    def deposit(self, amount: float) -> Decimal: 
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if decimal_amount > Account._qb:
            self._balance = self._balance + decimal_amount
            print("{} deposited".format(decimal_amount))
        return self._balance

    # hint that method takes float type
    def withdraw(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if Account._qb < decimal_amount <= self._balance:
            self._balance = self._balance - decimal_amount
            print("{} withdrawn".format(decimal_amount))
            return decimal_amount
        else:
            print("The amount must be greater than zero and more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance))

# tresting code to be run if file not run as module
if __name__ == '__main__':
    scott = Account("Scott")
    scott.deposit(10.1)
    scott.deposit(0.1)
    scott.deposit(0.1)
    scott.withdraw(0.3)
    scott.withdraw(0)
    scott.show_balance()

    print("*" * 80)