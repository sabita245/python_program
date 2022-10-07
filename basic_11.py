# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
user_input=int(input('enter an integer: '))
user_input_string=str(user_input)
# print(res[::-1])
# for i in range(len(user_input_string),0):
#     print(user_input_string[i],end=' ')
rev_str=''
for i in user_input_string:
    rev_str=i+' '+rev_str
print(rev_str)

