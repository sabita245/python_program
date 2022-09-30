string=input('enter the string')
string_new=string.split()
print(string_new)
string2=[]
for i in range(len(string_new)):
    if len(string_new[i])%2==0:
        string2.append(string_new[i])
print(' '.join(string2))
    