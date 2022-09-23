while True:
    try:
        age=int(input("enter your age: "))
        print(f'your age is {age}')
    except ValueError as err:
        print(f'enter a number {err}')
    else:
        print('Thank You!!')
        break