dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
current=0
prev=0
total=0
string=input('enter the roman value in capital: ')
for i in range(len(string)):
    current=dict[string[i]]
    if current>prev:
        total=total+current-(2*prev)
    else:
        total+=current
    prev=current
print(total)
