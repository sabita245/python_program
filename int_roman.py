def int_roman(num):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
    i=12
    roman_number=''
    while num!=0:
        if numbers[i]<=num:
            roman_number=roman_number+roman[i]
            num=num-numbers[i]
        else:
            i-=1
    return roman_number
num=int(input('enter a positive integer: '))
print(int_roman(num))