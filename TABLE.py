##ELECTRONICS SHOP MANAGEMENT SYSTEM##
##TABLE.py##
import mysql.connector as b
c=b.connect(host='localhost',user='root',passwd='admin')
d=c.cursor()
d.execute('use ESMS;')
d.execute('create table user(U_Name varchar(20),Password varchar(15), Name varchar(20),Ph_No int)')
d.execute('create table products(Prod_ID varchar(10),Prod_Name varchar(30),Quantity int,Price int)')
print('Table creation successful')
