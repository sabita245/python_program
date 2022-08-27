n=int(input("enter the number: "))
res=1
for i in range(n,0,-1):
    res=res*i
print("the factorial of ",n," is ",res)