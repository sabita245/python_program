class PlaySchool:
    membership=True
    def __init__(self,grade):
        self.grade=grade
    def attendance(self):
        print('60% attendance is mandetory.')
        print(f'k1 {self.grade}')
        return 'appreciated'

k1=PlaySchool('A')
k2=PlaySchool('R')
k3=PlaySchool('S')
k1.score=80
print(k1.grade)
print(k2.grade)
print(k3.grade)
print(k1.attendance())
print(k1.score)