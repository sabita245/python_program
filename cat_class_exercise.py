class OldestCat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def oldest(self):
        if self.age>3:
            print(f'The cat {self.name} is {self.age} years old')
            return 'done'
cat1=OldestCat('saira_cat',4)
cat2=OldestCat('kaira_cat',2)
cat3=OldestCat('mayra_cat',1)
#print(cat1.name)
#print(cat1.age)
print(cat1.oldest())
print(cat2.oldest())
print(cat3.oldest())