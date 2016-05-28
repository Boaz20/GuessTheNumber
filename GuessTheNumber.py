import random
print('--------------------')
print('GUESS THE NUMBER')
print('--------------------')
num=random.randint(0,100)
guess=-1
print (num)
while (num!=int(guess)):
    guess=input('Guess a number between 0 to 100: ')
print('YES! You got it! the number was',num)

