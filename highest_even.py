def highest_even(li):
    even_list=[]
    for i in li:
        if i%2==0:
            even_list.append(i)
    print(max(even_list))
print(highest_even([1,2,4,6,7,8,9]))