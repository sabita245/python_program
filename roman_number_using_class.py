class RomanNumber:
    def __init__(self,string):
        self.string=string
    def roman_number(self):
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        curr=0
        prev=0
        total=0
        for i in range(len(string)):
            curr=dict[string[i]]
            if curr>prev:
                total=total+curr-(2*prev)
            else:
                total+=curr
            prev=curr
        return total
string=input('enter the roman letter in capital: ')
obj=RomanNumber(string)
print(obj.roman_number())
