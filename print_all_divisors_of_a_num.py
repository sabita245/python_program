num=int(input('enter an integer: '))
res=[]
for i in range(1,num+1):
    rem=num%i
    if rem==0:
        print(i)
#print(res)
