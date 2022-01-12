## Hangman Game
import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # picks a random word from the file
    while "-" in word or ' ' in word:
        word = random.choice(word)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # function for letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()      # letters that the user guesses

    lives = 7 

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters that have been guessed
        # ' '.join(['a', 'b', 'c']) turns to 'a b c"
        print('You have' , lives, 'lives left and you have guessed these letters: ',' ' ' '.join(used_letters))

        # The current word as dashes (ex: F - - D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' ' ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if used_letters in word_letters:
                word_letters.remove(user_letter)
                print('')
        
            else:
                lives = lives - 1 # lose a live on a wrong guess
                print('\nYour letter is,', user_letter, 'is not in the word')

        elif user_letter in used_letters:
            print("You already guessed this letter. Please choose another letter.")
        
        else:
            print('Invalid character. Try again.')

    # this runs when the len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Congratulations! You have guessed', word, '!!')


hangman()
