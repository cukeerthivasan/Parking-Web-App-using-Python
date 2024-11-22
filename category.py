#!C:\Python312\python.exe
import cgi
import mysql.connector 
print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Added</h1>")
#1. Frontend to Backend
data=cgi.FieldStorage()
Companyname=data.getvalue("company")
Vehiclecategory=data.getvalue("category")
print("<i>",Companyname,Vehiclecategory,"</i>")
#2.Backend to Database

DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="parking"
)
mycursor=DB.cursor()
sql="INSERT INTO category(Companyname,Vehiclecategory) values (%s,%s)"
values=(Companyname,Vehiclecategory)
mycursor.execute(sql,values)
DB.commit()
print("</body>")
print("</html>")
