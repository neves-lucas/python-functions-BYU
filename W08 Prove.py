# W08 Prove Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Create a Wordle puzzle.

from os import system as clear
from time import sleep

# Variables
key_word = "moriancumer".lower()
trials = 0
game = True
count = 0
size = len(key_word)
hint = ''
letter = ''


clear('cls')
while game == True:
    print(f'Trials: {trials}')
    print()
    entry = str(input('Enter a word: ')).lower()
    trials += 1

    # Verifies if the user have won and congratulates him/her.
    # If he doesn't win, he will receive hints in the next turn.
    if entry == key_word:
        clear('cls')
        print(f'Key word: {key_word}')
        print(f'Trials: {trials}')
        print()
        print('Congratulations, you won!')
        game = False      
    
    else:
        # Puts underscores in the variable "hint".
        while count != size:
            letter = '_'
            hint += letter
            count += 1

        # Continuing trials. It only leaves the loop when the user types the correct word.
        while entry != key_word:
            count = 0
            letter = list()
            clear('cls')
            print(f'Trials: {trials}')
            print(f'Hint: {hint} ({size} letters.)')
            print()
            entry = str(input('Enter a word: ')).lower()

            # Validates if the user insert a word with a different number of letters.
            # It only continues if the numbers are equal.
            # Ex: Key word = love (4 letters)
            # Entry = battery (7 letters)
            # Result = False
            if len(entry) != size:
                clear('cls')
                trials += 1
                print(f'Trials: {trials}')
                print(f'Hint: {hint} ({size} letters.)')
                print()
                print('ERROR!!!')
                print(f'Please, insert a word with {size} leters.')
                sleep(2)
         
            else:
                clear('cls')
                trials += 1
                print(f'Trials: {trials}')
                print(f'Hint: {hint} ({size} letters.)')
                print()

                # It will loop according to the number of letters to go one by one.
                # Ex: TV (2 letters) = 2 loopings
                while count != size:
                    letter = ''
                    
                    # If the letter is in the right place, it will be upper case.
                    if entry [count] == key_word[count]:
                        letter = list(hint)
                        letter[count] = entry[count].upper()
                        hint = "".join(letter)
                        count += 1
                    
                    # If the letter exist in the key word, it will be lower case.
                    elif entry [count] in key_word:
                        letter = list(hint)
                        letter[count] = entry[count].lower()
                        hint = "".join(letter)
                        count += 1

                    # If the letter doesn't exist in the key word, put an "_".
                    else:
                        letter = list(hint)
                        letter[count] = '_'
                        hint = "".join(letter)
                        count += 1

               

        clear('cls')
        print(f'Key word: {key_word}')
        print(f'Trials: {trials}')
        print()
        print('Congratulations, you won!')
        game = False
        