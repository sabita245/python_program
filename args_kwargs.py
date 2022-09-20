from operator import itemgetter


def random_sum(*args,**kwargs):
    print(args)
    #return sum(kwargs.values())
    #return sum(args)
    total=0
    for item in kwargs.values():
        total=total+item
    return sum(args)+total

print(random_sum(1,2,3,4,num1=1,num2=3))