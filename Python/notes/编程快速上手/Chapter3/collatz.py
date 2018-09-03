#coding=utf-8
#Author = liu
import sys
def collatz(number):
    print(number)
    # if number % 2 == 0 :
    #     return print( number // 2 )
    # elif number % 2 == 1 :
    #     return print( 3 * number + 1)
    if number == 1:
        sys.exit()
    elif number % 2 == 1 :
        t = number * 3 + 1
        collatz(t)
    else:
        t = number // 2
        collatz(t)

if __name__ == '__main__':
    n = input('Enter number : ')
    try:
        n = int(n)
        collatz(n)
    except ValueError as verror:
        print('ValueError: You need input digital.')

