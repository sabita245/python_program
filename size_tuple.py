import sys
tu=(1,2,3)
print(len(tu))
print(sys.getsizeof(tu))
sum=0
for i in range(len(tu)):
    sum=sum+tu[i]
print(sum)
    
#print(sum)
