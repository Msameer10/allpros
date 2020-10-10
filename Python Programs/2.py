a=str(input("Enter Name of TEAM A:"))
b=str(input("Enter Name of TEAM B:"))
c=int(input("Enter Goals scored by TEAM A:"))
d=int(input("Enter Goals scored by TEAM B:"))
if(c>d):
    print(a,"WINS!")
elif(c<d):
    print(b,"WINS!")
else:
    print("Draw")
