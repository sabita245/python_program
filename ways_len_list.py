li=list(input('enter the list of numbers: '))
import time
#print(len(li))
start_time=time.time()
counter=0
for i in li:
    counter+=1
    end_time=time.time()
    ti=end_time-start_time
print(counter)
print(str(ti))

from operator import length_hint
# print(length_hint(li))