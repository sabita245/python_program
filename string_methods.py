#string=input('enter the string: ')
#print(string.capitalize())
#print(string.casefold())
# txt='banana'
# print(txt.center(20))
str1='hello hello hello123'
print(str1.count('l'))
print(str1.encode())
print(str1.endswith('o'))
print(str1.endswith('hello hello'))
txt=str1.find('e') #returns the first occurance index
print(txt)
print('welcome to my {0} program!'.format('python'))
print(str1.index('e'))
test='hello11'
print(test.isalnum())
test1='111'
print(test1.isdigit())
print(test.islower())
print(' '.join('hello python'))
li=['hello', 'summer','welcome!']
print(' '.join(li))
x='india'
x_lujst=x.ljust(7)
print(x_lujst,'is my country.')
x_rjust=x.rjust(7)
print('my country name is ',x_rjust)
x='hello Ram'
mytable=x.maketrans('R','s')
print(x.translate(mytable))
txt='I can see my country'
txt_new=txt.partition('the')
print(txt_new)
print(txt.split())
txt='   python is my lang   '
print(txt.strip())
txt='50'
x=txt.zfill(15)
print(x)