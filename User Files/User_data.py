f=open("Users.txt","a+")
Names=[]
for i in range(3):
    Name=input("Enter Your Name")
    Number=int(input(" Enter Your Phone Number"))
    Names=(str(Number),Name+'\n')
    f.writelines(Names)
f.close()
f=open("Man.txt","r")
Users=f.read()
print(Users)
