f=open("NUMBERS.txt","r")
Number=input("Enter Your Registered Mobile Number")
s=f.readlines()
L=len(s)
a=Number+'\n'
for i in range(L):
    if (s[i]==a):
        print("Welcome")

f.close()    
