import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if not guess.isdigit():
        raise Exception('Please enter 0 for tails, 1 for heads.')
toss = random.randint(0, 1) # 0 is tails, heads is 1
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

