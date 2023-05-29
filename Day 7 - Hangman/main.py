import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

#The user has 6 lives
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(len(chosen_word):
    display.append("_")

#Sets the number of blanks at a value greater than 0
nr_ = display.count("_")

#The user can keep guessing until the number of blanks is 0 (all the letter in the world have been guessed correctly) or the number of lives is greater than 0
while nr_ > 0 and lives > 0:
  guess = input("Guess a letter: ").lower()

#If the user has already chose the same letter
  if guess in display:
    print("You've already chosen this letter.")

#If the user chooses the right letter
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

#If the user chooses a letter not in the word (in this case the number of lives decreases by 1)
  if guess not in chosen_word:
    print(f'The letter "{guess}" is not in the word.')
    lives -= 1
    if lives == 0:
      print(f"You lose. The solution is '{chosen_word}'.")
  print(f"{' '.join(display)}")

#If there are no more blanks the user wins
  if "_" not in display:
    print("You win.")
    
  print(lives, hangman_art.stages[lives])
