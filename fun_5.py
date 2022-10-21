def even(item):
    return item%2==0
print(list(filter(even,[i for i in range(4,31)])))