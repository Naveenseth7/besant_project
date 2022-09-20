#onlinetickets
import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='online_tickets'
    
)
mycursor=mydb.cursor()
#mycursor.execute("create table bus_travels(fro_m varchar(20),T_o varchar(20), ticket_prize int)")
#query=("insert into bus_travels(fro_m,T_o,ticket_prize) values(%s,%s,%s)")
#value=("salem","thiruvannamalai",650)
#mycursor.execute(query,value)
#mycursor.execute("create table train(fro_m varchar(20),T_o varchar(20), ticket_prize int)")
#query=("insert into train(fro_m,T_o,ticket_prize) values(%s,%s,%s)")
#value=("madurai","delhi",8000)
#mydb.commit()

def bus():
    print("you have choosed for book tictects bus tickets")
    print("Choose the starting point of the bus travel")
    print("  CHENNAI -1\t MADURAI -2\n SALEM - 3")
    ustrt=int(input("plz enter your starting point :"))
    print("Choose the destination point to you reach :")
    print("Chennai- 1 \t Madurai-2\tKoyambattore-3\nSalem-4 \t vellore-5\tThiruvannamali-6")
    udest=int(input("plz enter your destination point :"))
    if(ustrt==1):
        ustrt="chennai"
    elif(ustrt==2):
        ustrt="madurai"
    elif(ustrt==3):
        ustrt="salem"
    else:
        print("insufficient input")
    if(udest==1):
        udest="chennai"
    elif(udest==2):
        udest="madurai"
    elif(udest==3):
        udest="koyambattore"
    elif(udest==4):
        udest="salem"
    elif(udest==5):
        udest="vellore"
    elif(udest==6):
        udest="thiruvannamalai"
    else:
        print("insufficient input")
    print(f"You are travelling from {ustrt} to {udest}")
    mycursor.execute("""select ticket_prize from online_tickets.bus_travels where fro_m='%s' and T_o='%s'"""%(ustrt,udest))
    col=mycursor.fetchone()
    print(f"you need to pay {col} to book ticket")
    fee=int(input("Please enter the payment :"))
    
    print(f"ticket booked sucessfully for travelling from {ustrt} to {udest}!!!")
               
def train():
    print("you have choosed for  train tickets")
    print("Choose the starting point of the train travel")
    print("  CHENNAI -1\t MADURAI -2\n SALEM - 3")
    ustrt=int(input("plz enter your starting point :"))
    print("Choose the destination point to you reach :")
    print("Chennai- 1 \t Madurai-2\tKoyambattore-3\nSalem-4 \t vellore-5\t")
    udest=int(input("plz enter your destination point :"))
    if(ustrt==1):
        ustrt="chennai"
    elif(ustrt==2):
        ustrt="madurai"
    elif(ustrt==3):
        ustrt="salem"
    else:
        print("insufficient input")
    if(udest==1):
        udest="chennai"
    elif(udest==2):
        udest="madurai"
    elif(udest==3):
        udest="koyambattore"
    elif(udest==4):
        udest="salem"
    elif(udest==5):
        udest="vellore"
    else:
        print("insufficient input")
    print(f"You are travelling from {ustrt} to {udest}")
    mycursor.execute("""select ticket_prize from online_tickets.train where fro_m='%s' AND T_o='%s'"""%(ustrt,udest))
    result= mycursor.fetchone()
    print(f"you need to pay {result} to book ticket")
    fee=int(input("Please enter the payment :"))
    
    print(f"ticket booked sucessfully for travelling from {ustrt} to {udest}!!!")

def flight():
    print("you have choosed for  flight tickets")
    print("Choose the starting point of the flight travel")
    print("  CHENNAI -1\t Madurai-2")
    ustrt=int(input("plz enter your starting point :"))
    print("Choose the destination point to you reach :")
    print("Delhi-1\t Mumbai-2\tKolkatta-3")
    udest=int(input("plz enter your destination point :"))
    if(ustrt==1):
        ustrt="chennai"
    elif(ustrt==2):
        ustrt="madurai"
    else:
        print("insufficient input")
    if(udest==1):
        udest="delhi"
    elif(udest==2):
        udest="mumbai"
    elif(udest==3):
        udest="kolkatta"
    else:
        print("insufficient input")
    print(f"You are travelling from {ustrt} to {udest}")
    mycursor.execute("""select ticket_prize from online_tickets.flight where fro_m='%s' AND T_o='%s'"""%(ustrt,udest))
    result= mycursor.fetchone()
    print(f"you need to pay {rusult} to book ticket")
    fee=int(input("Please enter the payment :"))
    
    print(f"ticket booked sucessfully for travelling from {ustrt} to {udest}!!!")
######################################################################################
name=""
id=""
password=""
login=0
print("Welcome  to our website..Have a great journey!!!")
ul=int(input(" press 1 for login, press 0 for singup : "))
if(ul==0):
     uname= input("Plz Enter your name :")
     uid= int(input("Set your id number :"))
     upwd= input("plese set your password :")
   
     name=uname
     password=upwd
     id=uid
     values=(name,id,password)
     sql=("insert into online_tickets.data(name,id,password) values(%s,%s,%s)")
     mycursor.execute(sql,values)
     mydb.commit()
     print("New id created successfully!!!")
     print(" To book bustickets press 1\n To book train tickets press 2\nTo book flight tickets press 3")
     ui=int(input("plz enter your choice :"))
     if(ui==1):
         bus()
     elif(ui==2):
         train()
     elif(ui==3):
         flight()

elif(ul==1):
    uid=int(input("please enter your id number: "))
    upwd=input("please enter your password : ")
    mycursor.execute("select * from online_tickets.data where id='%s'"%(uid))
    row=mycursor.fetchone()
    if mycursor.rowcount == 1:
        mycursor.execute("select * from online_tickets.data where password='%s'"%(upwd))
        row=mycursor.fetchone()
        if mycursor.rowcount == 1:
            login=1
            print("login successfully")

if(login==1):
    print(" To book bustickets press 1\n To book train tickets press 2\nTo book flight tickets press 3")
    ui=int(input("plz enter your choice :"))
    if(ui==1):
        bus()
    elif(ui==2):
        train()
    elif(ui==3):
        flight()
else:
    print("login faliled")

mydb.commit()





   
