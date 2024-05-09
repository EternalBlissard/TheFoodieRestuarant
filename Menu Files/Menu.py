import mysql.connector as Customer
from decimal import Decimal 
mycon=Customer.connect(host='localhost',user='root',passwd='Chai@123',database='SchoolProject')
if (mycon.is_connected()==True):
    pass
cursor=mycon.cursor()
cursor.execute("select * from menu ORDER BY Price ASC")
a=cursor.fetchall()
Item=[tuple(str(item)for item in t)for t in a]
L=len(a)
print("Dish Name","Price",sep="\t")
for i in range(0,L):
    print(Item[i][0],Item[i][1],sep='\t')
