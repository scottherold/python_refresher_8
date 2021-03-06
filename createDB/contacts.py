import sqlite3

# creates DB is it doesn't exist
# semi-colons from SQL are not necessary with the SQLite library
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Scott', 6545678, 'scott@email.com')")
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@myemail.com')")

# cursors allow programming languages to access SQL data
# cursors are an efficient method of accessing data as they don't use
# memory to access data
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# fetchall() creates a list of all the data in the DB
# print(cursor.fetchall())

# fetchone() returns a single row of data from teh DB
# print(cursor.fetchone()) # returns the first row
# print(cursor.fetchone()) # returns the second row
# print(cursor.fetchone()) # returns northing because there is no data

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close() # closes the stream
db.commit() # commits the changes to the DBs
# need to close the DB connection once finished (like a stream in I/O)
db.close()