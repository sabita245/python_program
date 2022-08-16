num=int(input("enter the number:"))
number=num
result=0
n=len(str(num))
while(num!=0):
    digit=num%10
    result=result+(digit**n)
    num=num//10
if(result==number):
    print("Given number is an armstrong number")
else:
    print("print given number is not an armstrong number")