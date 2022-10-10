from turtle import done, shape


class Matrix:
    def __init__(self,shape):
        self.shape=shape
    def hello(self):
        print(f'the shape of statue is {self.shape}')
        return 'done'
obj1=Matrix('circle')
#print(obj1.hello())
print(hasattr(obj1,'name'))
print(getattr(obj1,'shape'))
print(setattr(obj1,'shape','round'))
print(getattr(obj1,'shape'))
#delattr(obj1,'shape')
print(getattr(obj1,'shape'))
print(Matrix.__dict__)
print(Matrix.__doc__)
print(Matrix.__base__)
print(Matrix.__module__)