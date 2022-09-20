some_list=['a','b','c','b','d','m','n','n','a']
duplicate=[]
for i in some_list:
    if some_list.count(i) >1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)    
    
    
