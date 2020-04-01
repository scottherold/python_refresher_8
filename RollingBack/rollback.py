# Bank account examples (with data)
# since working with floats results in rounding errors, you can utilize
# working with decimals (see rollback2.py) or work with integers using
# cents, which will not result in rounding errors (as does with floats)

# Database connection added
import sqlite3
import pytz
import datetime

# DB Connection/Setup
db = sqlite3.connect("accounts.sqlite")
# PK is a composite key, instead of a ID column (for demonstrative
# purposes)
# this example of balance breaks with database normalization rules (no
# duplication of data). Normalization would use math to compute all
# depost/withdraw entries (you've done this before), but for performance
# reasons, storing an actual DB entry for balance eventually makes more
# sense, as computing massive amounts of deposit/withdraw amounts would
# be very memory intensive eventually
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER"
           " NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT"
           " NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):
    """ This class represents a bank account
    Static Methods:
        current_time: Returns a timestamp for data storage.

    Attributes:
        name (str): The name of the bank account
        balance (int): The current acount balance in cents

    Methods:
        save_update: Processes transaction amount received from the argument. Updates the account's
            instance's balance with the amount, and generates a new transaction.
        deposit: Checks if amount provided as argument is above 0, if true then amount is added to
            the the account instance's balance attribute and the amount is returned.
        withdraw: Checks if amount provided as argument is above 0 and above the account instance's
            balance attribute. If true, the account instance's balance attribute is reduced by the
            amount and the amount is returned. If false, a statement is printed notifying the user
            of the withdraw parameters and 0.0 is returned.
        show_balance: Prints the account instance's current name and balance.
    """
    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # # applies timezone to timestamp
        # return local_time.astimezone() 

    def __init__(self, name: str, opening_balance: int = 0):
        # open stream to DB
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        # check if row exists, if not create new account entry in DB
        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            # create new account using name provided, and default
            # opening balance
            cursor.execute("INSERT INTO  accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit() # saves the data
            print("Account created for {}. ".format(name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        trans_time = Account._current_time()
        # update balance for account
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        # add new transaction
        db.execute("INSERT INTO transactions VALUES(?, ?, ?)", (trans_time, self.name, amount))
        db.commit()
        self._balance = new_balance

    # refactored to work with a DB
    def deposit(self, amount: int) -> float: 
        if amount > 0.0:
            self._save_update(amount)
            # .2f tells python to display a float with two 0's following
            # the decimal
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    # hint that method takes float type
    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
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
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


# tresting code to be run if file not run as module
if __name__ == '__main__':
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    scott = Account("Scott")
    bob = Account("Bob", 9000)
    eric = Account("Eric", 7000)

    # close DB stream
    db.close()