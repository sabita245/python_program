my_list=['a','b','b','c','n','d','n']
res=[i for i in my_list if my_list.count(i)>1]
print(list(set(res)))