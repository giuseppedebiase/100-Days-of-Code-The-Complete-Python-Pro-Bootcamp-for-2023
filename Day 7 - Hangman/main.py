import random
import hangman_words
#imports logo and hangman art from the file hangman_art
import hangman_art

#imports one of the word from the file hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blanks, so that the user will see a series of _ equal to the number of letters in the chosen word
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Check if the user had already chosen the same letter
    if guess in display:
      print("You've already chosen this letter.")
    #Check guessed letter and substitute it to the blanks
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
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
