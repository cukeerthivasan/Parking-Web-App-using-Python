#!C:\Python312\python.exe
import cgi
import mysql.connector 
print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Added</h1>")
#1. Frontend to Backend
data=cgi.FieldStorage()
VehicelCategory=data.getvalue("category")
VehicleCompany=data.getvalue("company")
RegistrationNumber=data.getvalue("regnumber")
OwnerName=data.getvalue("name")
OwnerContactNumber=data.getvalue("num")
print("<i>",VehicelCategory,VehicleCompany,RegistrationNumber,OwnerName,OwnerContactNumber,"</i>")
#2.Backend to Database

DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="parking"
)
mycursor=DB.cursor()
sql="INSERT INTO addvehicle(VehicelCategory,VehicleCompany,RegistrationNumber,OwnerName,OwnerContactNumber) values (%s,%s,%s,%s,%s)"
values=(VehicelCategory,VehicleCompany,RegistrationNumber,OwnerName,OwnerContactNumber)
mycursor.execute(sql,values)
DB.commit()
print("</body>")
print("</html>")