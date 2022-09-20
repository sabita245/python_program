from functools import total_ordering
from tkinter import Y


x=0
def test():
    total=100
    global x
    x+=1
    print(x)
#test()
print(x)
test()
test()
print(test())
#without using global keyword
y=0
def demo(y):
    y+=1
    return y
print(demo(demo(demo(y))))