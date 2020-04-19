import random

levels = print('''
A - Easy
B - Medium
C - Hard
''')
player_level = input('Choose level: ').upper()

# function for easy level
def easy():
    computer_number = random.randint(1, 10)
    try:
        if player_level == 'A':
            player_guess = int(input('Guess a number from 1 to 10: '))
            guess_count = 0
            guess_limit = 6
            guess_left = 6
            if 10 >= player_guess >= 1:
                while player_guess != computer_number:
                    guess_count += 1
                    guess_left -= 1
                    if guess_count < guess_limit:
                        print(f'Wrong guess. You have {guess_left} guess(es) left')
                        player_guess = int(input('Try again: '))
                    else:
                        print('Game over!')
                        break
                else:
                    print('You got it right!')
                    # break
            else:
                print('Number is out of range!')
    except ValueError:
        print('That is not a number')


# function for medium level
def medium():
    computer_number = random.randint(1, 20)
    try:
        if player_level == 'B':
            player_guess = int(input('Guess a number from 1 to 20: '))
            guess_count = 0
            guess_limit = 4
            guess_left = 4
            if 20 >= player_guess >= 1:
                while player_guess != computer_number:
                    guess_count += 1
                    guess_left -= 1
                    if guess_count < guess_limit:
                        print(f'Wrong guess. You have {guess_left} guess(es) left')
                        player_guess = int(input('Try again: '))
                    else:
                        print('Game over!')
                        break
                else:
                    print('You got it right!')
                    # break
            else:
                print('Number is out of range!')
    except ValueError:
        print('That is not a number')


# function for hard level
def hard():
    computer_number = random.randint(1, 50)
    try:
        if player_level == 'C':
            player_guess = int(input('Guess a number from 1 to 50: '))
            guess_count = 0
            guess_limit = 3
            guess_left = 3
            if 50 >= player_guess >= 1:
                while player_guess != computer_number:
                    guess_count += 1
                    guess_left -= 1
                    if guess_count < guess_limit:
                        print(f'Wrong guess. You have {guess_left} guess(es) left')
                        player_guess = int(input('Try again: '))
                    else:
                        print('Game over!')
                        break
                else:
                    print('You got it right!')
                    # break
            else:
                print('Number is out of range!')
    except ValueError:
        print('That is not a number')


if player_level == 'A':
    print(easy())
elif player_level == 'B':
    print(medium())
elif player_level == 'C':
    print(hard())
else:
    print('Please choose a valid command!')
