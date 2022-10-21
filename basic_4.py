# Write a program to remove characters from a string starting from zero up to n and return a new string.
#remove first n characters from a string
# For examp
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
def remove_nchar(string,n):
    res=string[n:]
    return res
string=(input('enter a string'))
n=int(input('enter the number of char you want to remove'))
print(remove_nchar(string,n))