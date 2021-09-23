##ELECTRONICS SHOP MANAGEMENT SYSTEM##
##MAIN.py##
import sys
from datetime import datetime
import mysql.connector as a
d=a.connect(host='localhost',user='root',passwd='admin')
e=d.cursor()
e.execute('use ESMS;')
print('WELCOME')
def pg_1():
    print('1_LOGIN')
    print('2_CREATE ID')
    print('3_VIEW USERS')
    print('4_EXIT')
    b=int(input('PLEASE ENTER OPTION:'))
    if b==1:
        login()
    elif b==2:
        cid()
    elif b==3:
        vu()
    elif b==4:
        sys.exit()
    else:
        print('##INVALID OPTION##')
        pg_1()
def login():
    b=input('Enter your username:')
    c=input('Enter your password:')
    e.execute('select Password from user where U_Name="{}";'.format(b))
    f=e.fetchall()
    print(f)
    if f[0][0]==c:
        pg_2()
    else:
        print('##INCORRECT USERNAME OR PASSWORD##')
        print('##PLEASE RETRY##')
        login()
def cid():
    u=input('Enter username:')
    e.execute('select U_Name from user;')
    k=e.fetchall()
    e.execute('select count(U_Name) from user;')
    m=e.fetchall()
    j=int(m[0][0])
    l=[]
    for i in range(0,j):
        o=list(k[0][i])
        l=l+o
    if u in l :
        print('##USERNAME ALREADY EXISTS##')
        print('##PLEASE LOGIN##')
        pg_1()
    else:
        b=input('Enter password:')
        c=input('Enter your name:')
        f=eval(input('Enter your phone number:'))
        n=str(f)
        if 999999999<f<10000000000:
            com='insert into user values ("'+u+'","'+b+'","'+c+'",'+n+')'
            e.execute(com)
            d.commit()
            print('##PLEASE LOGIN TO CONTINUE##')
            login()
        else:
            print('##INVALID PHONE NUMBER##')
            print('##PLEASE RETRY##')
            cid()
def vu():
    e.execute('select Name,Ph_No from user;')
    f=e.fetchall()
    print(f)
    pg_1()
def pg_2():
    print('HELLO')
    print('1_BILLING')
    print('2_STOCK')
    print('3_LOGOUT')
    b=int(input('PLEASE ENTER OPTION:'))
    if b==1:
        bill()
    elif b==2:
        stock()
    elif b==3:
        pg_1()
    else:
        print('##INVALID OPTION##')
        pg_2()
def bill():
    e.execute('use BILLS;')
    m=datetime.now()
    z=m.strftime("%d%m%y_%H%M")
    e.execute('create table BILLED{}(Prod_ID varchar(10),Prod_Name varchar(30),Quantity int,Price int,Amount int)'.format(z))
    newitem(z)
def newitem(z):
    e.execute('use ESMS;')
    w=input('Enter product ID:')
    e.execute('select * from products where Prod_ID="{}";'.format(w))
    y=e.fetchall()
    if y==[]:
        print('##Invalid Product ID##')
        print('##Please retry##')
        newitem(z)
    else:
        f=int(input('Enter Quantity:'))
        e.execute('select Quantity from products where Prod_ID="{}";'.format(w))
        t=e.fetchall()
        num=int(t[0][0])
        if num<f:
            print('##Insufficient Quantity##')
            print('Please try again')
            newitem(z)
        g=int(input('Are you sure?(YES=1\\NO=2):'))
        if g==1:
            e.execute('use BILLS;')
            e.execute('insert into BILLED{} values("{}","{}",{},{},{});'.format(z,w,y[0][1],f,y[0][3],f*y[0][3]))
            d.commit()
            e.execute('use ESMS;')
            e.execute('update products set Quantity=Quantity-{} where Prod_ID="{}";'.format(f,w))
            k=int(input('Do you want to add more products?(YES=1\\NO=2'))
            if k==1:
                newitem(z)
            elif k==2:
                e.execute('use BILLS;')
                e.execute('select * from BILLED{};'.format(z))
                print(e.fetchall())
                e.execute('select sum(Amount) from BILLED{}'.format(z))
                at=e.fetchall()
                am=at[0][0]
                print('Total Amount is '+str(am))
                print('Thanks.....Come Again')
                e.execute('use esms;')
                pg_2()
            else:
                print('##Invalid option##')
                print('##Please retry##')
                newitem(z)
        elif g==2:
            newitem()
        else:
            print('##Invalid option##')
            print('##Please retry##')
            newitem()
            
def stock():
    print('1_VIEW')
    print('2_EDIT')
    print('3_BACK')
    z=int(input('Enter choice:'))
    if z==1:
        view()
    if z==2:
        edit()
    if z==3:
        pg_2()
def edit():
    print('1_ADD')
    print('2_MODIFY')
    print('3_DELETE')
    print('4_BACK')
    z=int(input('Enter choice:'))
    if z==1:
        add()
    if z==2:
        modi()
    if z==3:
        dele()
    if z==4:
        stock()
def view():
    e.execute('select * from products;')
    print(e.fetchall())
    stock()
def add():
    z=input('Enter Product ID:')
    e.execute('select * from products where  Prod_ID = "{}";'.format(z))
    v=e.fetchall()
    if v!=[]:
        print('##Product ID already Exists##')
        print('##Please Retry##')
        add()
    else:
        z=z
        y=input("Enter Product name:")
        x=input('Enter Quantity:')
        w=input('Enter Price:')
        e.execute('insert into products values("{}","{}",{},{});'.format(z,y,x,w))
        d.commit()
        e.execute('select * from products;')
        print(e.fetchall())
        print('Sucessfully Added')
        edit()
def dele():
    z=input('Enter product ID to be deleted:')
    e.execute('select * from products where  Prod_ID = "{}";'.format(z))
    v=e.fetchall();
    if v!=[]:
        print(v)
        x=int(input('Are you sure to delete this entry?(YES 1/NO 0):'))
        if x==1:
            e.execute('delete from products where Prod_ID ="{}";'.format(z))
            d.commit()
            e.execute('select * from products;')
            print(e.fetchall())
            print('Entry with Product ID ',z,' deleted sucessfully')
        else:
            print('No entries deleted')
            edit()
    else:
        print('No entries found...')
        print('##Please retry##')
        dele()
def modi():
    z=input('Enter product ID to be modified:')
    e.execute('select * from products where  Prod_ID = "{}";'.format(z))
    v=e.fetchall();
    if v!=[]:
        print('1_Change product name:')
        print('2_Change price')
        print('3_Change Quantity')
        print('4_Back')
        x=int(input('Enter the option:'))
        if x==1:
            cpn(z)
        elif x==2:
            cp(z)
        elif x==3:
            cq(z)
        elif x==4:
            edit()
        else:
            print('Enter valid option...')
            modi()
    else:
        print('Invalid Product ID')
        modi()
def cpn(ID):
    e.execute('select * from products where Prod_ID="{}";'.format(ID))
    print(e.fetchall())
    z=input('Enter new Product Name:')
    x=eval(input('Confirm Edit?(YES=1\\NO=2):'))
    if x==1:
        e.execute('update products set Prod_Name="{}" where Prod_ID = "{}";'.format(z,ID))
        d.commit()
        e.execute('select * from products where Prod_ID="{}";'.format(ID))
        print(e.fetchall())
        print('Successfully updated')
        modi()
    else:
        modi()
def cp(ID):
    e.execute('select * from products where Prod_ID="{}";'.format(ID))
    print(e.fetchall())
    z=int(input('Enter new Price:'))
    x=int(input('Confirm Edit?(YES=1\\NO=2):'))
    if x==1:
        e.execute('update products set Price={} where Prod_ID = "{}";'.format(z,ID))
        e.execute('select * from products where Prod_ID="{}";'.format(ID))
        d.commit();
        print(e.fetchall())
        print('Successfully updated')
        modi()
    else:
        modi()
def cq(ID):
    e.execute('select * from products where Prod_ID="{}";'.format(ID))
    print(e.fetchall())
    z=int(input('Enter new Quantity:'))
    x=int(input('Confirm Edit?(YES=1\\NO=2):'))
    if x==1:
        e.execute('update products set Quantity={} where Prod_ID = "{}";'.format(z,ID))
        e.execute('select * from products where Prod_ID="{}";'.format(ID))
        print(e.fetchall())
        d.commit()
        print('Successfully updated')
        modi()
    else:
        modi()
pg_1()




