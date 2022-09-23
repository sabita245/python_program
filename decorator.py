def my_decorator(func):
    def wrap_fun():
        print('*************')
        func()
        print('*************')
    return wrap_fun   
@my_decorator
def hello(greeting):
    print(greeting)
hello('good morning!')