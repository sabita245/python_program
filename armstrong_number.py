for i in range(1000):
    num=i
    n=len(str(i))
    result=0
    while(i!=0):
        digit=i%10
        result=result+(digit**n)
        i=i//10
    if(num==result):
        print(num,end=' ')