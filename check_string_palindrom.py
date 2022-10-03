string=input('enter a string: ')
print(string[::-1])
if string==string[::-1]:
    print('its a palindrome string')
else:
    print('not palindrome string')