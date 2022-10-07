# Create a new list from a two list using the following condition
# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
#li=[odd(li1)+even(li2)]
li1=[1,2,3,4,5]
li2=[5,12,34,2,89,11]
li1_odd=[i for i in li1 if i%2!=0]
li2_even=[i for i in li2 if i%2==0]
li=li1_odd+li2_even
print(li)