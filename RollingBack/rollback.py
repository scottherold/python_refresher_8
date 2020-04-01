# Bank account examples (with data)
# since working with floats results in rounding errors, you can utilize
# working with decimals (see rollback2.py) or work with integers using
# cents, which will not result in rounding errors (as does with floats)
class Account(object):
    """ This class represents a bank account 
    
    Attributes:
        name (str): The name of the bank account
        balance (int): The current acount balance in cents

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

    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = opening_balance
        print("Account created for {}".format(name), end='')
        self.show_balance()

    # hint that method takes float type
    def deposit(self, amount: int) -> float: 
        if amount > 0.0:
            self._balance += amount
            # .2f tells python to display a float with two 0's following
            # the decimal
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    # hint that method takes float type
    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            # .2f tells python to display a float with two 0's following
            # the decimal
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero and more than your account balance")
            return 0.0

    def show_balance(self):
        # .2f tells python to display a float with two 0's following
            # the decimal
        print("Balance on account {} is {:.2f}".format(self.name, self._balance 
            / 100))

# tresting code to be run if file not run as module
if __name__ == '__main__':
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()