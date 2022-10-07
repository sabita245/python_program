# from collections import OrderedDict
dict={1:'a',5:'b',3:'t',2:'g'}
#print(dict.get('c',6))
# print(OrderedDict(sorted(dict.items())))
# def dict():
#     key_values={}
#     key_values[1]='a'
#     key_values[5]='b'
#     key_values[2]='r'
#     key_values[0]='t'
#     for i in sorted(key_values.keys()):
#         print(i,end=' ')
# def main():
#     dict()
# if __name__=='__main__':
#     main()
for i in sorted(dict.keys()):
    print(i,dict[i])
    

# dict={}
# dict[1]='abc'
# dict[2]='xyz'
# dict[1]='pqr'
# print(dict)
dict={'a':1,'b':2,'c':3,'d':4,'e':5}
li=list(dict.values())
print(li)
sum=0
for i in li:
    sum=sum+i
print(sum)
list=[
    {'name':'nandini','age':28},
    {'name':'manjeet','age':22},
    {'name':'nikhil','age':23}
]
print(sorted(list,key= lambda i: i['age'],reverse=True))


