import mysql.connector as Customer
from decimal import Decimal 
mycon=Customer.connect(host='localhost',user='root',passwd='yourPasswd',database='SchoolProject')
if (mycon.is_connected()==True):
    pass
cursor=mycon.cursor()

def HOME():
    print("Welcome to Funtastia: The Vegetarian Restustrant")
    print("What would you like to do?")
    print("1.Reserve a table")
    print("2.Food PickUp")
    print("3.Check Offers")
    print("4. Our Menu")
    print("5. Admin Login")
    print("6. Profile")
    print("7. Exit")
    print("Please enter ur choice by entering the number before your choice")
    Choice=input("Enter Your Choice")
    if (Choice=="1"):
        Reserve()
    if (Choice=="2"):
        PICK_UP()
    if (Choice=="3"):
        Offers()
    if (Choice=="4"):
        Menu_Buffet()
    if (Choice=="5"):
        Update_Menu()
    if (Choice=="6"):
        Profile()
    if(Choice=="7"):
        print("See You Next Time")
def Reserve():
    a=input("Have you registered with us if YES then type YES otherwise type NO")
    if (a=="YES"):
        Name=Profile_Checker()
        Date=Date_Selector()
        Time=Time_Slots()
        People=int(input("Enter NO. of People"))
        print("Dear",Name)
        print("You have successfully booked a Table for",People,"at",Date,"on",Time)
        cursor.execute("insert into Reservation values('{}',{},'{}','{}',{})".format(Name,Phone_Number,Time,Date,People))
        mycon.commit()
        print("Redirecting You to Home")
        HOME()
    elif(a=="NO"):
        print("Please create a profile before Reserving a Table")
        Profile_Creator()
        Reserve()
    else:
        print("Try Again")
        Reserve()
def Profile_Creator():
    Name=input("Enter your name")
    Phone_Number=input("Enter Your Phone Number")
    print("Optional To Add DOB and Email")
    Choice_Email=input("Want to Add Your Email YES/NO")
    if (Choice_Email=='YES'):
        Email=input("Enter Your Email Address")
    else:
        Email=''
    Choice_DOB=input("Want to Add Your Date Of Birth/DOB YES/NO")
    if (Choice_DOB=='YES'):
        DOB=Date_Of_Birth()
        cursor.execute("insert into CustomerInfo values({},'{}','{}','{}')".format(Phone_Number,Name,Email,DOB))
        mycon.commit()
    else:
        cursor.execute("insert into CustomerInfo values({},'{}','{}',NULL)".format(Phone_Number,Name,Email))
        mycon.commit()
    print("Profile has been created Successfully")
        
def Profile_Checker():
    global Phone_Number
    Phone_Number=int(input("Enter Phone Number"))
    
    flag=cursor.execute('select * from CustomerInfo where PhoneNumber='+str(Phone_Number))
    c=cursor.fetchall()
    if (len(c)==1):
        return c[0][1]
    else:
        print("Number NOt Found")
        HOME()
def PICK_UP():
    a=input("Have you registered with us if YES then type YES otherwise type NO")
        
    if (a=="YES"):
        global Name
        Name=Profile_Checker()
        MENU_PICKUP()
        a=input("Ready to Order?YES/NO")
        if(a=="YES"):
            FOOD_NAME=input("Enter the Name of the Food Item You want to order")
            ORDER(FOOD_NAME)
            x=input("Wanna Add Something Else???YES/NO")
            while(x=="YES"):
                print("Please Enter the Spelling Correctly and In Capital Letters")
                FOOD_NAME=input("Enter the Name of the Food Item You want to order")
                ORDER(FOOD_NAME)
                x=input("Wanna Add Something Else???YES/NO")
        elif(a=="NO"):
            print("OK, TAKING YOU BACK")
        else:
            print("We didn't get you?")
        print("Order is being processed")
        Bill()
        print("Taking You Back to Home")
        HOME()
    elif(a=="NO"):
        print("Please create a profile before Reserving a Table")
        Profile_Creator()
        PICK_UP()
    else:
        print("Try Again")
        PICK_UP()
def MENU_PICKUP():
    cursor.execute("select * from menu ORDER BY Price ASC")
    a=cursor.fetchall()
    Item=[tuple(str(item)for item in t)for t in a]
    L=len(a)
    print("Dish Name","Price",sep="\t")
    for i in range(0,L):
        print(Item[i][0],Item[i][1],sep='\t')
def ORDER(a):
    cursor.execute("select * from menu where Itemname ='{}' ".format(a))
    c=cursor.fetchall()
    if (len(c)==1):
        Product_Price=c[0][1]
        Quantity=int(input("How much of these?"))  
        ORDER_COST.append(Product_Price)
        COSTUMER_ORDER.append(a)
        ORDER_QUANTITY.append(Quantity)
    else:
        print("Try Again Pls")
        HOME()
def Bill():
    Bill=0
    L=len(COSTUMER_ORDER)
    print("FOOD ITEM","QUANTITY","COST",sep="\t")
    for i in range(0,L):
        print(COSTUMER_ORDER[i],ORDER_QUANTITY[i],ORDER_COST[i],sep="\t")
        Bill+=ORDER_QUANTITY[i]*ORDER_COST[i]
    cursor.execute("insert into Sales values('{}',{})".format(Name,Bill))
    mycon.commit()
    print("Your Order is PLaced Successfully")
    print("Please Pay ",Bill,"While Collecting your Order")
def Offers():
    print("NO Running Offers at the moment")
    HOME()
def Menu_Buffet():
    cursor.execute("select * from menu")
    a=cursor.fetchall()
    Item=[tuple(str(item)for item in t)for t in a]
    L=len(a)
    print("Dish Name")
    for i in range(0,L):
        print(Item[i][0],sep='\t')
def Date_Of_Birth():
    Date=int(input("Enter Date"))
    Month=int(input("Enter Month"))
    Year=int(input("Enter Year"))
    flag=1
    if(Date>0 and (Month>0 and Year>0)):
        if(Month<=12):
            if(Date<=28):
                pass
            elif(Month in [1,3,5,7,8,10,12]):
                if(Date<=31):
                    pass
                else:
                    flag=0
            elif(Month in [4,6,9,11]):
                if(Date<=30):
                    pass
                else:
                    flag=0
            elif(Year%4==0):
                if(Month==2):
                    if(Date==29):
                        pass
                    else:
                        flag=0
                else:
                    flag=0
            else:
                flag=0
        else:
            flag=0
    else:
        flag=0
    if(flag==0):
        print("Invalid Date ")
    if(flag==1):
        if (Month<10):
            if (Date<10):
                Date_Final=str(Year)+'-'+'0'+str(Month)+'-'+'0'+str(Date)
                return Date_Final
            else:
                Date_Final=str(Year)+'-'+'0'+str(Month)+'-'+str(Date)
                return Date_Final
        else:
            if (Date<10):
                Date_Final=str(Year)+'-'+str(Month)+'-'+'0'+str(Date)
                return Date_Final
            else:
                Date_Final=str(Year)+'-'+str(Month)+'-'+str(Date)
                return Date_Final
def Update_Menu():
        
    Admin=input("Enter Admin Username")
    Password=input("Enter Admin Password")
    if (Admin=="Wolf"):
        if (Password=="Wolfie"):
            print("You have successfully Logged In")
            Logged_In()
def Logged_In():
    print("What Do You Wanna Do?")
    print("1. Change an items price")
    print("2. Delete An Item From the List")
    print("3. Add an Item To The List")
    print("4. Go Back to HOME")
    print("5. End the Application")
    print("Enter from Choice as the Number before Your Choice")
    Choice_Update=input("Enter Choice")
    if (Choice_Update=='1'):
        Price_Updater()
    elif(Choice_Update=='2'):
        Item_Deleter()
    elif(Choice_Update=='3'):
        Item_Adder()
    elif(Choice_Update=='4'):
        HOME()
    elif(Choice_Update=='5'):
        print("You Have Successfully Ended the Application")
def Price_Updater():
    Menu_Buffet()
    Item=input("Enter Name of Item whose Price is to Be Changed")
    cursor.execute("select * from menu where Itemname ='{}' ".format(Item))
    c=cursor.fetchall()
    if (len(c)==1):
        Product_Price=c[0][1]
        print("Current Price",Product_Price)
        Choice=input("Do You Want to change the price??? YES/NO")
        if(Choice=="YES"):
            Price=int(input("Enter the Price Of the Item"))
            cursor.execute("UPDATE menu SET Price={} WHERE ItemName='{}'".format(Price,Item))
            print("Price Updated")
            Price_Updater()
        else:
            Logged_In()
def Date_Selector():
    Date=int(input("Enter Date"))
    Month=int(input("Enter Month"))
    Year=int(input("Enter Year"))
    flag=1
    if(Date>0 and (Month>0 and Year>0)):
        if(Month<=12):
            if(Date<=28):
                pass
            elif(Month in [1,3,5,7,8,10,12]):
                if(Date<=31):
                    pass
                else:
                    flag=0
            elif(Month in [4,6,9,11]):
                if(Date<=30):
                    pass
                else:
                    flag=0
            elif(Year%4==0):
                if(Month==2):
                    if(Date==29):
                        pass
                    else:
                        flag=0
                else:
                    flag=0
            else:
                flag=0
        else:
            flag=0
    else:
        flag=0
    if(flag==0):
        print("Invalid Date ")
        Date_Selector()
    elif(Year<2021):
        print("Enter a date After 1 Jan 2021")
        flag=0
        Date_Selector()
    if(flag==1):
        if (Month<10):
            if (Date<10):
                Date_Final=str(Year)+'-'+'0'+str(Month)+'-'+'0'+str(Date)
                return Date_Final
            else:
                Date_Final=str(Year)+'-'+'0'+str(Month)+'-'+str(Date)
                return Date_Final
        else:
            if (Date<10):
                Date_Final=str(Year)+'-'+str(Month)+'-'+'0'+str(Date)
                return Date_Final
            else:
                Date_Final=str(Year)+'-'+str(Month)+'-'+str(Date)
                return Date_Final
            
def Time_Slots():
    print("We have Reservations for a Maximum of 1.5 hours")
    print("At Every Half an Hour from 10:00 to 21:30")
    print("Minutes should be either 0 or 30")
    print("Enter Time in 24 Hour Clock Format")
    Hours=int(input("Enter Hour"))
    Minutes=int(input("Enter Minutes"))
    flag=0
    if((Hours<=24 and Hours>=0) and (Minutes<60 and Minutes>=0) ):
        flag=1
        if (Hours<10):
            print("Sorry We Open At 10:00")
            flag=0
        elif(Hours>22):
            print("Sorry The Last Slot that You Can Book is for 21:30 ")
            flag=0
        elif(Minutes%30!=0):
            print("You can book Slots at Hours:00 or Hours:30 ")
            flag=0
        else:
            pass
    if(flag==0):
        print("Invalid Time")
        Time_Slots()
    elif(flag==1):
        if(Minutes>0):
            Time=str(Hours)+':'+str(Minutes)
        else:
            Time=str(Hours)+':'+str(Minutes)+'0'
            
        return Time
def Item_Deleter():
    Menu_Buffet()
    Item=input("Enter Name of Item which is to be Deleted")
    cursor.execute("select * from menu where Itemname ='{}' ".format(Item))
    c=cursor.fetchall()
    if (len(c)==1):
        Product_Price=c[0][1]
        print("Current Price",Product_Price)
        Choice=input("Do You Want to delete this item??? YES/NO")
        if(Choice=="YES"):
                
            cursor.execute("DELETE FROM menu WHERE ItemName='{}'".format(Item))
            mycon.commit()
            print("Item Deleted Successfully")
            Item_Deleter()
        elif(Choice=="NO"):
            Item_Deleter()
        else:
            print("Unable to Understand You")
            Logged_In()
    else:
        print("Error")
        Logged_In()
def Item_Adder():
    
    Menu_Buffet()
    Choice=input("Do You Want to Add an item to the Menu??? YES/NO")
    if(Choice=="YES"):
        Item=input("Enter Name of Item which is to be Added")
        Price=int(input("Enter the Price of the Item"))
        cursor.execute("insert into menu values('{}',{})".format(Item,Price))
        mycon.commit()
        print("Item Added Successfully")
        Item_Adder()
    elif(Choice=="NO"):
        Logged_In()
def Profile():
    Profile_Checker()
    print("Welcome ")
    print("You have Logged in Successfully")
    Profile_Viewer()
    Profile_Changer()
def Profile_Changer():
    print("Choose whatever you want to do with your profile")
    print("1.View Profile")
    print("2. Edit Your Profile")
    print("3. Delete Profile")
    print("4. Go Back to Home")
    print("5. End the process")
    Choice=int(input("Enter the number before your desired choice"))
    if(Choice==1):
        Profile_Viewer()
    elif(Choice==2):
        Profile_Editor()
    elif(Choice==3):
        Profile_Deleter()
    elif(Choice==4):
        HOME()
    elif(Choice==5):
        print("You have successfully ended the process")
    else:
        print("Enable to Understand You")
        print("Please Try Again")
        HOME()
        
def Profile_Viewer():
    flag=cursor.execute('select * from CustomerInfo where PhoneNumber='+str(Phone_Number))
    c=cursor.fetchall()
    if (len(c)==1):
        print("Phone Number",Phone_Number)
        print("Name",c[0][1])
        if(c[0][2]==''):
            print("Email","-")
        else:
            print("Email",c[0][2])
        if(c[0][3]==''):
            print("Date of Birth","-")
        else:
            print("Date of Birth",c[0][3])
    else:
        print("Error")
        HOME()
def Profile_Deleter():
    Choice=input(("Do you really want to delete your profile??YES/NO"))
    if (Choice=="YES"):
        cursor.execute("DELETE FROM CustomerInfo WHERE PhoneNumber='{}'".format(Phone_Number))
        mycon.commit()
        print("Your Profile has been deleted Succesfully")
        print("We are sad to see you go ")
        print("We hope to see you Again")
    elif(Choice=="NO"):
        print("Alright Your Profile Won't Be Deleted")
    else:
        Profile_Changer()
def Profile_Editor():
    print("Choose what you want to update in your profile")
    print("1.Phone Number")
    print("2.Name")
    print("3.Email")
    print("4.Date of Birth")
    print("5. Go to Home")
    print("6. Go Back")
    Choice=int(input("Enter the number before your desired choice"))
    if(Choice==1):
        print("Phone Number cannot be changed")
        print("Delete the this profile and create a new one in order to change your Phone Number")
        Profile_Deleter()
    elif(Choice==2):
        Name=input("Enter your new Name")
        cursor.execute("UPDATE CustomerInfo SET CustomerName='{}' WHERE PhoneNumber={}".format(Name,Phone_Number))
        mycon.commit()
        print("Your New Profile",Profile_Viewer())
        Profile_Editor()
    elif(Choice==3):
        Email=input("Enter your new Email")
        cursor.execute("UPDATE CustomerInfo SET CustomerName='{}' WHERE PhoneNumber={}".format(Email,Phone_Number))
        mycon.commit()
        print("Your New Profile",Profile_Viewer())
        Profile_Editor()
    elif(Choice==4):
        DOB=Date_Of_Birth()
        cursor.execute("UPDATE CustomerInfo SET DOB='{}' WHERE PhoneNumber={}".format(DOB,Phone_Number))
        mycon.commit()
        print("Your New Profile",Profile_Viewer())
        Profile_Editor()
    elif(Choice==5):
        HOME()
    elif(Choice==6):
        Profile_Changer()
    else:
        print("Unable to Understand You")
        print("Try Again")
        Profile_Editor()
def Profile_Number():
    PhoneNumber=input("Enter New Phone Number")
    cursor.execute("UPDATE CustomerInfo SET PhoneNumber='{}' WHERE PhoneNumber={}".format(PhoneNumber,Phone_Number))
    mycon.commit()
    Phone_Number=PhoneNumber
    print("Your New Profile",Profile_Viewer())
COSTUMER_ORDER=[]
ORDER_QUANTITY=[]
ORDER_COST=[]
HOME()  
