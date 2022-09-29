li1=list(input('enter the first list: '))
li2=list(input('enter the second list: '))
def common(li1,li2):
    res=False
    for x in li1:
        for y in li2:
            if x==y:
                res=True
                return res
    return res
print(common(li1,li2))
