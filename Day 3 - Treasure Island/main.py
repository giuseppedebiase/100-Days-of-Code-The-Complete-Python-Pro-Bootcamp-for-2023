print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("What direction do you want to take? Left or right?\n").lower()
if direction == "left":
  lake = input("You find yourself in front of a lake, do you want to swim through it or do you want to wait? Write 'swim' or 'wait'\n")
  if lake == "wait":
    door = input("You find three doors: a red one, a blue one and a yellow one. Which one do you want to open? Write 'red', 'blue' or 'yellow'\n")
    if door == "red":
      print("The room behind the door was on fire. The backfire sets you ablaze. Game Over")
    elif door == "blue":
      print("The room behind the door was full of water. A shark exit through the door and eats you. Game Over.")
    elif door == "yellow":
      print("You found the treasure!")
    else:
      print(f"An unreliable narrator narrates this game. There is indeed a {door} door. Behind this door you find a bunny brooding a colorful egg. Nice find!")
  else:
    print("A crocodile eats you. Game Over.")
else:
  print("You fall through a hole. Game Over.")
