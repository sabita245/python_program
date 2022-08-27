n=int(input("enter the number: "))
first=0
second=1
print(first)
print(second)
for i in range(n):
    temp=first
    first=second
    second=(temp+first)
    print(second)
print()