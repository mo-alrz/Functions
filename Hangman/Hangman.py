import random
from words import words


def choose_words(words):
    my_word = random.choice(words).lower()
    while '-' in my_word or ' ' in my_word:
        my_word = random.choice(words)

    return my_word


def hang_man():
    new_word = list(choose_words(words).lower())
    my_word_listed = ['-'] * len(new_word)
    print(*my_word_listed)
    wrong_choices = []
    while '-' in my_word_listed:

        user_choice = input('Enter a Character : ')
        if user_choice in wrong_choices:
            print(f'That was chosen before')
        elif user_choice in new_word:
            index_user_choice = new_word.index(user_choice)
            new_word[index_user_choice] = 0
            my_word_listed[index_user_choice] = user_choice
        else:
            wrong_choices.append(user_choice)
        print(*wrong_choices)

        print(*my_word_listed)
    print('Congrats, you completed the world')


hang_man()
