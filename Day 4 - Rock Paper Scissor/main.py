rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("Rock, paper or scissors? Type '0' for rock, '1' for paper and '2' for scissors.\n"))
computer_choice = random.randint(0,2)
sign = [rock, paper, scissors]
if choice < 0 or choice >= 3:
  print("Invalid number, you lose.")
elif (computer_choice == choice-1) or (computer_choice == 2 and choice == 0) :
  print(sign[choice])
  print("Computer chose:")
  print(sign[computer_choice])
  print("You win!")
elif computer_choice == choice:
  print(sign[choice])
  print("Computer chose:")
  print(sign[computer_choice])
  print("It's a draw!")
else:
  print(sign[choice])
  print("Computer chose:")
  print(sign[computer_choice])
  print("You lose!")
