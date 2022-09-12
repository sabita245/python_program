li=[1,2,3,4,5]
print(li)
li1=li[:] #copy using : slice operator
print(li1)
li2=[]
li2.extend(li1) #copy using extend()
print(li2)
li3=li2 #copy using assignmnet = operator
print(li3)
li4=[i for i in li3] #copy using list compreshion
print(li4)
li5=li4.copy() # copy using copy()
print(li5)