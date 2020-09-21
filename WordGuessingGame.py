# Using the random module and choice method which returns a random element from a given sequence
from random import choice   

word = choice(('apple', 'grape', 'pear', 'almond', 'mango', 'pineapple', 'kiwi', 'watermelon', 'banana', 'lime'))

clue = word[0] + ' & ' + word[::-1][0]      #gives a clue as the first and last letter of the random word

word_guess = ''
store_letter = ''       # stores guessed letters
count = 0       # Initialize count
attempt = 2     

print('Welcome to "Guess the Word Game!" We are guessing names of fruits.')

print('\nINSTRUCTIONS: You have 2 attempts at guessing the letters and a final attempt at guessing the name of the fruit.')
print("Let's begin!!!")
print('\n')

# print('\n') prints a newline,

while count < attempt:
    letter_guess = input('Guess a letter: ').lower()
    if len(letter_guess) >= 2:
        print('Input only a letter!')
    count += 1      # Increment count

    if letter_guess in word:
        print('Yes!')
        store_letter += letter_guess        # Adds the correct letter to the stored letters

    else:
        print('No!')

    if count == 2:      # After 2 attempts
        print('\n')
        clue_request = input('Would you like a clue? [yes / no]: ').lower()

        if clue_request == 'yes':
            print('\n')
            print('CLUE: The first and last letter of the fruit is: ', clue)

        elif clue_request == 'no':
            print("Alright then!")

print('\n')
print('You have guessed', len(store_letter), 'letters correctly.')
print('These letters are: ', store_letter)

word_guess = input('Now guess the whole word: ').lower()

if word_guess.lower() == word:
    print('Congratulations, you guessed right!')
else:
    print("Oops, that's wrong! The answer was,", word)
    

print('\n')
input('Press Enter to leave the program')
