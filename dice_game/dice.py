import random
import os
def number_die():
    while True:
        num = input('How many dice do you want to play: between 1-2: ')
        num_die =  ['1', 'one', 'two', '2']
        try:
            if num not in num_die:
                raise ValueError('please, enter a number between 1-2 or there spelling in words')
            else:
                return num
        except ValueError as err:
            print(err)
def roll_dice():
    min_value  = 1
    max_value = 6
    roll_again = 'y'
    while roll_again.lower()  in ('y', 'yes'):
        os.system('cls' if os.name == 'nt' else clear)
        amount = number_die()
        if amount == '2' or amount == 'two':
            print(f'You chose {2} dice to play your game')
            first_dice = random.randint(min_value, max_value)
            second_dice = random.randint(min_value, max_value)
            print('The first die value: ', first_dice)
            print('The second die value: ', second_dice)
            print('Total you got for rolling the two dice is: ', first_dice + second_dice)
            roll_again = input('Do you want to roll again: ')
        else:
            print(f'You chose {1} die to play your game')
            die = random.randint(min_value, max_value)
            print('The die value is: ', die)
            print('Total you got for rolling a die is: ', die)
            roll_again = input('Do you want to roll again: ')
if __name__ == '__main__':
    roll_dice()