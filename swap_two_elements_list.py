def swap_list(li,po1,po2):
    li[pos1],li[pos2]=li[pos2],li[pos1]
    return li
li=list(input('enter the list'))
pos1=int(input('enter the pos1:'))
pos2=int(input('enter the pos2:'))
print(swap_list(li,pos1,pos2))


