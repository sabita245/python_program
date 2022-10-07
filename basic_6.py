# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5
li=[1,2,3,4,5,25,15]
res=[i for i in li if i%5==0]
print(res)