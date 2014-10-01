from random import randint

print('come-out')
dice1 = randint(1, 6) 
dice2 = randint(1, 6) 
diceTotal = dice1 + dice2        
print(diceTotal)

if diceTotal == 7 or diceTotal == 11:
    print('You win!')
elif diceTotal == 2 or diceTotal == 3 or diceTotal == 12:
    print('Craps, you lose.')
else:
    print('The point is', diceTotal)
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    newDiceTotal = dice1 + dice2   
    print(newDiceTotal)
    
    while newDiceTotal != diceTotal and newDiceTotal != 7:
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        newDiceTotal = dice1 + dice2
        print(newDiceTotal)
        
    if newDiceTotal == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
