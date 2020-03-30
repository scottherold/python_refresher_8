import sqlite3

db = sqlite3.connect("contacts.sqlite")

# cursors can be used to get certain data, like updated rows
update_sql = "UPDATE  contacts SET email = 'update@update.com' WHERE contacts.phone = 1234"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))

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