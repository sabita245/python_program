li=[1,1,20,3,40,23,12,45]
# res=[]
# for i in li:
#     if i<10:
#         res.append(i)
# print(res)
res=[i for i in li if i < 10]
print(res)