import mysql.connector
con = mysql.connector.connect(host="localhost", user="root",password="root", database="school_db")
cur = con.cursor()
 
query = "INSERT INTO students VALUES (%s,%s, %s, %s,%s, %s)"
data = (5,5, "Priya", "B", "Science",91.0)
 
cur.execute(query, data)
con.commit()          # saves the change permanently
print("Record inserted")
con.close()
