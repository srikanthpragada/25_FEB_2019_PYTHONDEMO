import sqlite3

# Connect to database
try:
    con = sqlite3.connect(r"e:\classroom\python\feb25\hr.db")
    cur = con.cursor()
    id = input("Enter job id :")
    cur.execute("select title from jobs where id = ?", (id,))
    row = cur.fetchone()
    if row is None:
        print("Sorry! Job id not found")
    else:
        print("Title : ", row[0])
        newtitle = input("Enter new title :")
        cur.execute("update jobs set title = ? where id = ?", (newtitle, id))
        print("No. of rows updated : ", cur.rowcount)
        con.commit()
except Exception as ex:
    print("Error :", ex)
finally:
    con.close()
