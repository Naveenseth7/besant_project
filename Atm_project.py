
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='Atm'
    
)
mycursor=mydb.cursor()

#1 for login 0 for crearte account
name=""
account_num=""
password=""
depo_amount=0
def process():
             print(" press 1 for deposite amount\n press 2 for withdraw amoutnt \n press 3 for balance checking \n press 4 to change pasword \n press 5 to exit ")
             ui=int(input("enter your choice :"))
             if(ui==1):
                 ui2=int(input(f" Enter the amount you want to deposit in {uaccn}  account :"))
                 mycursor.execute("""select amount from Atm.data where acc_num='%s'"""%(uaccn))
                 col=mycursor.fetchone()
                 x=list(col)
                 for i in x:
                   p=(int(i))      
                   new=p+ui2
                #print(f"the value{new}") 
                 mycursor.execute("""update data set amount='%s' where acc_num='%s' """%(new,uaccn))
                 mydb.commit()
                 print("deposite successfully!!!")
             if(ui==2):
                 ui2=int(input(f" Enter the amount you want to withdraw in {uaccn}  account :"))
                 mycursor.execute("""select amount from Atm.data where acc_num='%s'"""%(uaccn))
                 col=mycursor.fetchone()
                 x=list(col)
                 for i in x:
                   p=(int(i))      
                   new=p-ui2
                #print(f"the value{new}") 
                 mycursor.execute("""update data set amount='%s' where acc_num='%s' """%(new,uaccn))
                 mydb.commit()
                 print("withdraw successfully!!!")
             if(ui==3):
                 mycursor.execute("""select amount from Atm.data where acc_num='%s'"""%(uaccn))
                 col=mycursor.fetchone()
                 x=list(col)
                 for i in x:
                   bal=(int(i))
                   print(f"Ur balance is {bal}")
             if(ui==4):
                nwpwd=input(f"Enter the new password for {uaccn} account :")
                mycursor.execute("""update data set password='%s' where acc_num='%s' """%(nwpwd,uaccn))
                print("password updated successfully!!!")
                mydb.commit()
             if(ui==5):
                 exit(0)
print("welcome to ABC Bank Atm")
l_i=int(input("press 1 for login & press 0 if you don't have any account"))

if(l_i==0):
    uname= input("Plz Enter your name :")
    uaccn= int(input("enter your account number :"))
    upwd= input("plese set your password :")
    udepo= int(input("intial amount must be more than 500 , please enter the first deposite amount:"))
    if(udepo>=500):
        name=uname
        password=upwd
        account_num=uaccn
        depo_amount=udepo
     
        val=(name,account_num,password,depo_amount)
        sql="insert into data(name,acc_num,password,amount) values(%s,%s,%s,%s)"
        mycursor.execute(sql,val)
        mydb.commit()
        process()
    else:
        print("sir, intial amount must be gretterthan 500")
elif(l_i==1):
     uaccn=int(input("please enter your account number: "))
     upwd=input("please enter your password : ")
     mycursor.execute("select * from Atm.data where acc_num='%s'"%(uaccn))
     row=mycursor.fetchone()
     if mycursor.rowcount == 1:
         mycursor.execute("select * from Atm.data where password='%s'"%(upwd))
         row=mycursor.fetchone()
         if mycursor.rowcount == 1:
            print("login successfully")
            process()

         else:
             print("invalid password")
     else:
         print("invalid account number")
else:
     print("Enter a valid input!!")
mydb.commit


                
                     

    