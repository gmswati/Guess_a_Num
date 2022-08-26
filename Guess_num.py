from random import randint
from art import logo

# print(randint(1,100))
print(logo)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a no. between 1 and 100')
level=input("Enter The difficulty level ('easy' or 'hard'): ")
attempts=10
num=randint(1,100)
# print
# if level=='easy':
#     print(f'You have {attempts} attempts to guess the number.')
if level=='hard':
    attempts=5
print(f'You have {attempts} attempts to guess the number.')

while attempts>0:
    guess_num=int(input('Enter the guessed no.: '))
    if guess_num==num:
        print('You guessed absolutely correct.')
        print('congrates')
        break

    elif guess_num> num:
        print('It is too high.')

    else:
        print('It is too low.')
        # print('Guess again')
        # print(f'You have {attempts} attempts to guess the number.')

    attempts-=1
    print('Guess again')
    print(f'You have {attempts} attempts to guess the number.')
if attempts==0 and guess_num!=num:
    print('Sorry!,You loose the game')
    print(f'The number was {num}')
