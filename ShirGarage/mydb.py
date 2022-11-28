import sqlite3
from turtle import update
con = sqlite3.connect("ShirGarage.db")
cur = con.cursor()
# cur.execute("create TABLE treatments(treatmentID ,employeeName, customerName, treatmentType)")
# cur.execute("""
# insert into treatments
# VALUES
# (2, 'alon', 'roee', '15,000 treatment')
# """)
cur.execute("""
update treatments
set treatmentType = '20,000 treatment'
where treatmentID = 2 """)
con.commit()
res = cur.execute("SELECT * From employees")
print(res.fetchall())