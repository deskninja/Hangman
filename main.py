from replit import clear
import random
from hangman_art import logo, stages
from words import word_list


def get_guess(letters):
    user_input = input('guess a letter: ').lower()
    while len(user_input) != 1 or user_input in letters:
        if len(user_input) != 1:
            user_input = input('please input one letter!\nguess a letter: ').lower()
        elif user_input in guesses:
            user_input = input('you have already guessed that letter!\nguess a letter:').lower()

    return user_input


if __name__ == '__main__':
    chosen_word = random.choice(word_list)
    stage = len(stages) - 1
    guesses = []

    display = []
    for letter in chosen_word:
        display += "_"

    print(logo)
    print(display)

    while "_" in display and stage > 0:
        guess = get_guess(guesses)
        clear()
        guesses += guess

        found = False

        for index, letter in enumerate(chosen_word):
            if guess == letter:
                found = True
                display[index] = guess

        if not found:
            stage -= 1
            print(guess, ' is not in the word')
            print(stages[stage])

        print(display)

    if "_" not in display:
        print('you win')
    else:
        print(stages[stage])
        print('the word was ', chosen_word)
        print('you lose, try again :(')
