# script to check DB contents
import sqlite3
# import pytz

# db connect; detect_types tells sqlite to perform a conversion back
# into the the data type that was declared when the data was saved into
# the DB.
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# query data; use sqlite built in strftime function to localize timezone
# this converts the datetime entry into a string. The function takes
# three arguments, the format you want outputted, the field that
# contains the datetime field and the timezone that you want
# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time,'localtime')"
#                       " AS localtime, transactions.amount FROM transactions"
#                       " ORDER BY transactions.time"):

# refactored due to VIEW being made in rollback.py
for row in db.execute("SELECT * FROM localtransactions"):
    print(row)

db.close()