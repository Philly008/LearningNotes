# -*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import random

def guess_fun():
    global guess
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails: ')
        guess = input()

guess = ''
guess_fun()
toss = random.choice(['heads', 'tails'])    # 0 is tails, 1 is heads
logging.info('toss is %s, guess is %s' % (toss, guess))
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    guess_fun()
    logging.info('toss is %s, guess is %s' % (toss, guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. Your are really bad at this game.')



# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails: ')
#     guess = input()
# toss = random.randint(0, 1)     # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     if toss == guess :
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')
#
