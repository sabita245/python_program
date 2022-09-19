def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the first integer: "))
b=int(input("enter the second integer: "))
gcd=gcd(a,b)
print("gcd of a&b :",gcd)
if gcd==1:
    print("both the integers are coprime")
else:
    print("both the integers are not co-prime")
 

