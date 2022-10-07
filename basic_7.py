# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

# Given:

# str_x = "Emma is good developer. Emma is a writer"
# Expected Output:

# Emma appeared 2 times
from collections import Counter
input_string='Emma is good developer. Emma is a writer'
count=Counter()
input_string_split=input_string.split()
sub_string='Emma'
print(input_string_split.count(sub_string))
