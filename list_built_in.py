def multiply_2(item):
    return item**2
print(list(map(multiply_2,[1,2,3]))) #used map()
def only_odd(item):
    return item%2!=0
print(list(filter(only_odd,[1,2,3,4,5,6]))) #used filter()
li1=[1,2,3,4,5]
li2=[i for i in li1 if i%2!=0]
print(list(zip(li1,li2)))#used map()
print(sorted(li1)) #used sorted()
li2_rev=reversed(li2) #used reversed()
li2_reversed=[i for i in li2_rev]
print(li2_reversed)
x=sum(li1) #used sum()
print(x)
x=ord('h')
print(x)





        