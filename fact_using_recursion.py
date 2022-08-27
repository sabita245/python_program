from math import factorial


def fact(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number: "))
res=fact(n)
print("The factorial of",n ,"is ",res)