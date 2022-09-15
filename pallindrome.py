string=input("enter the string: ")
rev_string=""
for i in string:
    rev_string=i+rev_string
if (string==rev_string):
    print("entered string is pallindrome")
else:
    print("entered string is not a pallindrome")