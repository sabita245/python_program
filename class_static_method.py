class PlayerCharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def run(self):
        print(f'my name is {self.name} and I am {self.age} years old')
        return 'done'
        
    @classmethod
    def adding_number(cls,num1,num2):
        return cls('teddy', num1 + num2 )
#print(PlayerCharacter.adding_number(2,5))
player1=PlayerCharacter.adding_number(3,4)
print(player1.age)
print(player1.run())

