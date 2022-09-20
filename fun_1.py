def driving_age(age):
    if age<18:
        print("You can drive when you become 18")
    elif age>18:
        print("power on! you can drive")
    elif age==18:
        print("You are welcome!")
    else:
        print("enter a valid age")
age=int(input("enter your age: "))
driving_age(age)