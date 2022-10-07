# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.
def list_value_same(li):
    if li[0]==li[-1]:
        return True
    else:
        return False
li=list(input('enter a list: '))
print(list_value_same(li))