from collections import Counter
user_input='''geeks for geeks'''
uniqw=Counter(user_input.split())
print(uniqw)
s=' '.join(uniqw.keys())
print(s)



