def reverse(string):
    rev_string=""
    for i in string:
        rev_string=i+rev_string
    print("reversed string is",rev_string)
string=input("enter the string:")
print("the entered string is",string)
reverse(string)
