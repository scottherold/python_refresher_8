# quick check for the contacts table
import sqlite3

conn = sqlite3.connect("contacts.sqlite")

# user input
user_name = input("Please enter your name ")

# example of passing a single argument to a tuple; you must include the
# trailing comma, or it will turn the single value provided into a tuple
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?",
    (user_name,)):
    print(row)

conn.close()