is_magician= True
is_expert= False
if is_magician and is_expert :
    print("you are the master in magic")
elif is_magician and not is_expert:
    print("atleast you are there")
else:
    print("you need magic power")
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)
for _ in range(4):
    print(list(range(10)))
for i,char in enumerate('hello'):
    print(i,char)