# Given two integer numbers return their produc
# only if the product is equal to or lower than 1000, else return their sum.
num1=int(input('enter first num: '))
num2=int(input('enter second number: '))
# prod=num1*num2
# if prod<=1000:
#     print(prod)
# else:
#     print(num1+num2)
def num_eval(num1,num2):
    if num1*num2 <=1000:
        return num1*num2
    else:
        return num1+num2
print(num_eval(num1,num2))