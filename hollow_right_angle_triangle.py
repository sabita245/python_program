n=int(input("enter numb: "))
for i in range(n):
    print('* ',end='')
    if(i>=2 and i!=(n-1)):
        print(' '*(i) + '* ',end='')
    else:
        print('* ' * i,end='')
    print()