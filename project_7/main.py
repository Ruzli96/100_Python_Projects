import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

prev_guess = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in prev_guess:
        print(f'The letter \"{guess}\" has already been used')
    else:
        prev_guess.append(guess)

    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f'The letter \"{guess}\" is not in the word, You lose a life')
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])