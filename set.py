b=set()
print(len(b))
print(type(b))
b.add(4)
b.add(5)
b.add((1,2,3))
# b.add({'a':1,'c':6})
# print(b)
b.union({2,3})
print(b)