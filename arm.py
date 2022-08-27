for i in range(100):
    num=i
    res=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        res=res+(digit**n)
        i=1//10
    if(res==num):
        print(num)