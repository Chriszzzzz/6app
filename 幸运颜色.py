import random

colors = ['red', 'blue','green', 'purple','yellow']
luckcolor = random.choice(colors)

for i in range(3):
    print('There are {} colors'.format(colors))
    guess = input('Guess your lucky color: ')
    if guess != luckcolor:
        print('Seems like {} is not your lucky color:('.format(guess))
        colors.remove(guess)
    else:
        break

if guess == luckcolor:
    print('Great!{} is your lucky color'.format(luckcolor))
else:
    print('Actually, {} is your lucky color!'.format(luckcolor))
