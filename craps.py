from random import randint

print('come-out')
r1 = randint(1, 6) #bad use Intention-Revealing Names
r2 = randint(1, 6) #bad
v = r1 + r2        #bad use Intention-Revealing Names
print(v)           #use searchable names
if v == 7 or v == 11:
    print('You win!')
elif v == 2 or v == 3 or v == 12:
    print('Craps, you lose.')
else:
    print('The point is', v)
    r1 = randint(1, 6)
    r2 = randint(1, 6)
    w = r1 + r2   #use destictive names v & w
    print(w)
    while w != v and w != 7:
        r1 = randint(1, 6)
        r2 = randint(1, 6)
        w = r1 + r2
        print(w)
    if w == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
