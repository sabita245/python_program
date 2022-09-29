from random import randint
answer=randint(1,10)
#print(answer)
guess_input=int(input('enter a random integer'))
if guess_input==answer:
    print('correct answer')
else:
    print('sorry, enter another number.')