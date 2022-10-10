cat_ages=[]
class OldestCat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        cat_ages.append(self.age)
    def oldest():
        return max(cat_ages)
cat1=OldestCat('cathy',12)
cat2=OldestCat('rubby',10)
cat3=OldestCat('cyani',8)
print(f'the oldest cat is {OldestCat.oldest()}')
