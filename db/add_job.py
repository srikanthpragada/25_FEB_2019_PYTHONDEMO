import sqlite3

# Connect to database
try:
    con = sqlite3.connect(r"e:\classroom\python\feb25\hr.db")
    cur = con.cursor()
    row = (5,'Web Designer',5000,50000)
    cur.execute("insert into jobs values(?,?,?,?)", row)
    print("No. of rows inserted : ", cur.rowcount)
    con.commit()
except Exception as ex:
    print("Error :", ex)
finally:
    con.close()
