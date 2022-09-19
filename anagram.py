string1=input("enter the first string: ")
string2=input("enter the second string: ")
#string1.sort()
print("string1 is:",string1)
print("string2 is:",string2)
if(list(sorted(string1))==list(sorted(string2))):
    print("both the strings are anagram")
else:
    print("both the strings are not anagrem")