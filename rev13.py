for i in range(1000):
    num=i
    res=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        res=res+(digit ** n)
        i=i//10
    if(res==num):
        print(num)