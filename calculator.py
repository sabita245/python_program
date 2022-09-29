num1=int(input('enter the first number: '))
num2=int(input("enter the second number"))
def addition(num1,num2):
    return num1+num2
def substraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
dict={1:"add",2:"substraction",3:"multiplication",4:"division"}
print('please choose an action below: ',dict)
action=input()
if action=='1':
    print(addition(num1,num2))
elif action=='2':
    print(substraction(num1,num2))
elif action=='3':
    print(multiplication(num1,num2))
elif action=='4':
    print(division(num1,num2))
else:
    print("please enter a correct option")

