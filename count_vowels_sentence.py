string=input("enter the sentence:")
string=string.lower()
count=0
vowel_list=["a","e","i","o","u"]
for i in string:
    if i in vowel_list:
        count+=1
print(count)