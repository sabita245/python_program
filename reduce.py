from functools import reduce
my_list=[1,2,3]
def accumulate(acc,item):
    print(acc,item)
    return acc+item
print(reduce(accumulate,my_list,0))

