class User():
    def sign_in(self):
        print('logged in!')
    def __init__(self,email):
        self.email=email
class Wizard(User):
    def __init__(self,name,age,email):
        User.__init__(self,email)
        self.name=name
        self.age=age
    def attack(self):
        #User.attack(self)
        print(f'name of player is {self.name} and age is {self.age} & email {self.email}')
class Archery(User):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def attack(self):
        print(f'name of player is {self.name} and age is {self.age}')
wizer1=Wizard('John',50,'john@gmail.com')
#print(wizer1.attack())
archer1=Archery('Teddy',39)
#print(archer1.attack())
#print(isinstance(wizer1,Wizard))
#print(isinstance(archer1,User))
#print(isinstance(wizer1,object))
###polymorphism-------------------
""" def player_attack(char):
    char.attack()
print(wizer1.attack())
print(archer1.attack()) """
for char in [wizer1,archer1]:
    print(char.attack())
