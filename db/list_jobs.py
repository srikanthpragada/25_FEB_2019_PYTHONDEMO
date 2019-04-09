import sqlite3

# Connect to database
con = sqlite3.connect(r"e:\classroom\python\feb25\hr.db")
cur = con.cursor()
# Execute sql command
cur.execute("select * from jobs")
# take one row (tuple) at a time from cursor
for row in cur.fetchall():
    print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")

cur.execute("select * from jobs order by title")
print("\nJobs\n")
for id, title, min, max in cur.fetchall():
    print(f"{id:5d} - {title:30s} - {min:5d} - {max:5d}")

con.close()
