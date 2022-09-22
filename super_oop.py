class User:
    def __init__(self,email):
        self.email=email
    def sign_in(self):
        print("logged in!")
class Wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self,email)
        #super().__init__(self,email)
        self.name=name
        self.power=power
    def attack(self):
        print(f'the player named {self.name} have power of {self.power} whose email is {self.email}')
class Archer(User):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(f'the player named {self.name} has {self.power} arraows left.')
wizard1=Wizard('John',50,'john@gmail.com')
archer1=Archer('shaan',60)
print(wizard1.attack())
print(archer1.attack())