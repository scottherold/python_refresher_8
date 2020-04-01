# script to check DB contents
import sqlite3
import pytz

# db connect; detect_types tells sqlite to perform a conversion back
# into the the data type that was declared when the data was saved into
# the DB.
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# query data
for row in db.execute("SELECT * FROM transactions"):
    utc_time = row[0]
    # converts to local timezone (from time saved) using pytz
    local_time = pytz.utc.localize(utc_time).astimezone()
    print("{}\t{}".format(utc_time, local_time))

db.close()