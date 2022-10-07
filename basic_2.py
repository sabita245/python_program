# Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.
# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
def sum_num(num):
    for i in range(1,num+1):
        print(f'sum of {i} and its previous number {i-1} is: ',i+(i-1))
print(sum_num(5))
