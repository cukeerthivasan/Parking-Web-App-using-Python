#!C:\Python312\python.exe
import cgi
import mysql.connector 
print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Logined</h1>")
#1. Frontend to Backend
data=cgi.FieldStorage()
Name=data.getvalue("username")
Mobilenumber=data.getvalue("mobile")
Emailaddress=data.getvalue("mail")
Password=data.getvalue("pass")
print("<i>",Name,Mobilenumber,Emailaddress,Password,"</i>")
#2.Backend to Database

DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="parking"
)
mycursor=DB.cursor()
sql="INSERT INTO login(Name,Mobilenumber,Emailaddress,Password) values (%s,%s,%s,%s)"
values=(Name,Mobilenumber,Emailaddress,Password)
mycursor.execute(sql,values)
DB.commit()
print("</body>")
print("</html>")
