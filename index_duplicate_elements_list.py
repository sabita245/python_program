li=list(input("enter the list:"))
char=input("enter the char you want find duplicate index:")
print(li)
li1=[i for i in range(len(li)) if li[i]==char]
print(li1)
