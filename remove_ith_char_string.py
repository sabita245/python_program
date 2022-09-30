string=input('enter the string: ')
pos=int(input('enter the pos: '))
new_str=""
for i in range(len(string)):
    if i!=pos:
        new_str=new_str+string[i]
print(new_str)
