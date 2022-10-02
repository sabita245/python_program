import sys
dict={1:'a',2:'w',3:'r'}
li=list(dict.keys())
sum=0
for i in range(len(li)):
    sum=sum+li[i]
print(sum)
print(str(sys.getsizeof(dict))+' '+'bytes')