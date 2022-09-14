n=int(input("enter the number: "))
res=0
for i in range(1,n):
    if(n%i==0):
        res=res+i
        #print(res)
if(res==n):
    print("perfet num")
else:
    print("not perfect number")
    