#Conecting MySql to python file

import mysql.connector
print("""
--------------------------------------------------------------------------------
                   *** Welcome to Courier Management Service ***
--------------------------------------------------------------------------------
""")
#Creating Database for my project

mydb=mysql.connector.connect(host="localhost",user="root",passwd='1912118128')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists Courier_Management")
mycursor.execute("use Courier_Management")
mycursor.execute("use Courier_Management")
mycursor.execute("create table if not exists login(username varchar(25) not null,password varchar(25)not null) ")
mycursor.execute("create table if not exists purchase(odate date not null, name varchar(25) not null,pcode int not null)")
mycursor.execute("create table if not exists store(pcode int not null, track_ID int not null,pdesc varchar(50), pweight int not null,destination_address varchar(100) not null, sender_address varchar(100) not null, shipping_cost int not null)")
mydb.commit()

#Entering Data when Database is Empty

z=0
mycursor.execute("select * from login")
for i in mycursor:
    z+=1
if (z==0):
    mycursor.execute(" insert into login values('username','1912') ")
    mydb.commit()

#Creating a Login System For Admin & user    
while True:
    print("""1.ADMIN
2.CUSTOMER
3.EXIT
             """)
    ch=int(input("Enter Your Choice: "))
    if(ch==1):
        passs=input("Enter Password: ")
        mycursor.execute("select * from login")
        for i in mycursor:
            username,password=i
        if(passs==password):
            print(" Welcome Admin ")
#creating Loop for continue at store part
            loop2='y'
            if(loop2=='y' or lopp2=='Y'):
                    print("""
    Press 1 - Add New Product
    Press 2 - Display All Couriered Products
    Press 3 - Search a Courier
    Press 4 - Delete a Courier
    Press 5 - To change the Password
    Press 6 - Log Out
    """)

    #Adding a product into database
                
    ch=int(input("Enter Your Choice: "))
    if(ch==1): 
                    loop='y'
                    while(loop=='y'or loop=='Y'):
                        
                        pcode=int(input("Enter Product code: "))
                        track_ID=int(input("Enter Tracking ID: "))
                        pdesc=input("Enter Product Description: ")
                        pweight=int(input("Enter Product Weight: "))
                        destination_address=input("Enter Destination Address: ")
                        sender_address=input("Enter Sender Address: ")
                        shipping_cost=int(input("Enter Cost of Shipping: "))
                        mycursor.execute("insert into store values('"+str(pcode)+"','"+str(track_ID)+"','"+pdesc+"','"+str(pweight)+"','"+destination_address+"','"+sender_address+"','"+str(shipping_cost)+"')")
                        mydb.commit()
                        print("Record Successfully Inserted...")
                        loop=input("Do you want to enter more items(y/n): ")
                    loop2=input("Do you want to continue editing store(y/n): ")

                    #Showing all couriered prodect
    elif(ch==2):                
                    mycursor.execute("Select * from store")
                    rows = mycursor.fetchall()
                    for row in rows:
                        print(row)

                        
                  #program to search a courier
    elif(ch==3):
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                        unique_ID = int(input("Enter Tracking_ID: "))
                        mycursor.execute("Select * from store where track_ID = %s",(unique_ID,))
                        result= mycursor.fetchone()
                        if result is not None:
                             print("Data found",result)
                        else:
                            print("Tracking ID Not Found...")
                        loop=input("Do you want to find other data(y/n): ")
                    loop2=input("Do you want to continue editing store(y/n): ")
                     
                    
                    #Deliting Items from Database
                    
    elif(ch==4):
                        loop='y'
                        while(loop=='y' or loop=='Y'):
                            pcode=int(input("Enter product code: "))
                            mycursor.execute("delete from store where pcode='"+str(pcode)+"'")
                            mydb.commit()
                            loop=input("Do you want to delet any other data(y/n): ")
                        loop2=input("Do you want to continue editing store(y/n): ")

                    #writing program to change the password
    elif(ch==5):
                    old_Pass=input("Enter Old Password: ")
                    mycursor.execute("select * from login")
                    for i in mycursor:
                        username,password=i
                    if(old_pass==password):
                        new_Pass=input("Enter New Password: ")
                        mycursor.execute("update login set password='"+new_pass+"'")
                        mydb.commit()
                        print("Your Password has  Change ")
                    # for logout
    elif(ch==6):
                     break;

                    
    print("""
    Press 1 - Add New Product
    Press 2 - Display All Couriered Products
    Press 3 - Search a Courier
    Press 4 - Delete a Courier
    Press 5 - To change the Password
    Press 6 - Log Out
    """)

    #Adding a product into database
                
    ch=int(input("Enter Your Choice: "))
    if(ch==1):
                    pcode=int(input("Enter Product code: "))
                    track_ID=int(input("Enter Tracking ID: "))
                    pdesc=input("Enter Product Description: ")
                    pweight=int(input("Enter Product Weight: "))
                    destination_address=input("Enter Destination Address: ")
                    sender_address=input("Enter Sender Address: ")
                    shipping_cost=int(input("Enter Cost of Shipping: "))
                    mycursor.execute("insert into store values('"+str(pcode)+"','"+str(track_ID)+"','"+pdesc+"','"+str(pweight)+"','"+destination_address+"','"+sender_address+"','"+str(shipping_cost)+"')")
                    mydb.commit()
                    print("Record Successfully Inserted...")
    else:
             print("Wrong Password")
