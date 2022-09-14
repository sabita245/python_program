lower=int(input("enter the lower range:"))
upper=int(input("enter the upper range:"))
for num in range(lower,upper+1):
    res=0
    for i in range(1,num):
        if(num%i==0):
            res=res+i
    if(res==num):
        print(num)