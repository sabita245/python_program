def fun1(*args):
    return args
print(fun1(1,2,34))
def calculation(num1,num2):
    return (num1+num2),(num1-num2)
print(calculation(40,10))
def emp(name,salary=9000):
    return (f'{name}:{salary}')
print(emp('jalsa'))
print('saira:',12000)
################
def outer(a,b):
    def add(a,b):
        return a+b
    res=add(a,b)
    return res+5
print(outer(2,3))
print(101//10)