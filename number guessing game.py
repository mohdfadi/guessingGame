import random
random_number = random.randint(1,7)
chance = 0
while chance <5:
    player = int(input('guess a number between 1 and 7\nEnter: '))
    if player == random_number:
         print('You won!')
         print('Computer guessed'+' '+ str(random_number))
         break
    else:
        chance+=1
    if chance ==5:
         print('You Lose!')
         print('Computer guessed'+' '+str(random_number))
        