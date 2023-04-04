# Rock/paper/scissors

import random


def play(x):
    """ x is the number that player wants to play in a game """
    counter = 0
    wins_by_you = 0
    wins_by_pc = 0
    ties = 0

    while counter < x:
        user_choice = input("'r' for rock,'p' for paper and 's' for scissors : ")
        if user_choice not in ['r', 'p', 's']:
            continue
        if user_choice in ['r', 'p', 's']:
            counter += 1
            com_choice = random.choice(['r', 'p', 's'])

            if (user_choice == 'r' and com_choice == 's') \
                    or (user_choice == 'p' and com_choice == 'r') \
                    or (user_choice == 's' and com_choice == 'p'):
                wins_by_you += 1
                print('You win')

            elif user_choice == com_choice:
                ties += 1
                print('Tie')

            else:
                wins_by_pc += 1
                print('Computer Wins')

        if counter == x:
            print(f'Your wins : {wins_by_you}'
                  f' Computer wins : {wins_by_pc}'
                  f' Ties : {ties}')


play(5)
