string=input('enter a string: ')
print(f'the given string is {string}')
length=int(len(string)/2)
print(length)
str1=string[0:length]
print(str1)
str2=string[length:]
print(str2)
if str1==str2:
    print('the given string is symmetric.')
elif str1==str2[::-1]:
    print('the given string is a palindrome')
else:
    print('enter a string only!')