n=int(input("n:"))
for i in range(n):
    print('  ' * i + '* ',end='')
    if i!=(n-1):
        print('  '*(2*n-2*i-3)+'*',end='')
    print()