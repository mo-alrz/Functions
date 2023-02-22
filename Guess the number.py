# Write a program that stores a number and the user has to figure it out
# The user can input guesses but the number of guesses is limited
# After each guess the program would tell one of the following:
#
# The stored number is higher
# The stored number is lower
# You found the number: 8
# Game over : If user can not find the number during the allowed guesses

import random


def guess(x, y, allowed_num_of_guesses):

    num = random.randint(x, y)
    num_of_guesses = 0

    while num_of_guesses != allowed_num_of_guesses:

        user_guess = int(input('Guess the number : '))
        num_of_guesses += 1

        if user_guess == num:
            print('Congratulations , You found the number :', num)
            break

        elif user_guess > num:
            print('The stored number is lower')

        elif user_guess < num:
            print('The stored number is higher')

    if num_of_guesses == allowed_num_of_guesses:
        print('Game Over')


guess(1, 20, 5)
