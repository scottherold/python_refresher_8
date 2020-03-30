import sqlite3

db = sqlite3.connect("contacts.sqlite")

# variables for SQL placeholders
new_email = "newemailupdate@update.com"
phone = input("Please enter the phone number ") # user input for SQL param

# cursors can be used to get certain data, like updated rows
# refactored with placeholders
# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
# refactored with shorthand placeholders instead of string formatting
# In sqlite, this is ?
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()
# execute script is designed for executing multiple SQL statements
# separate by a semi-colon. This is succeptiable to SQL injection
# attacks
# update_cursor.executescript(update_sql)
# refactored to allow parameter substituion
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}\n".format(update_cursor.connection == db))

# if using a cursor, call the commit method using the cursor's
# connection property
update_cursor.connection.commit()
update_cursor.close()

# python allows you to iterate through collections without manually
# setting up a cursor. Python automaticaly creates a cursor with the
# connection to the DB.
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

db.close()