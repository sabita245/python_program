def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print(gcd(a,b))