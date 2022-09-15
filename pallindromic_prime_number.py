num=int(input("enter the number:"))
rev_number=int(str(num)[::-1])
print(rev_number)
for i in range(2,rev_number):
    if(rev_number%i==0):
        print("not pallindromic prime number")
        break
else:
    print("entered number is a pallindromic prime numer")