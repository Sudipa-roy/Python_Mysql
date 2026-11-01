import mysql.connector
 
con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="school_db"
)
 
if con.is_connected():
    print("Connected to MySQL successfully")
else:
    print("Connection failed")
 
con.close()
