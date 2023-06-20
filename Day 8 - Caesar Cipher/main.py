alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

def caesar(direction, text, shift):
  if shift > 26:
    shift = shift % 26
  generated_text = ""
  for char in text:
    if char not in alphabet:
      generated_text += char
    else:
      position = alphabet.index(char)
      if direction == "encode":
        new_position = position + shift
      elif direction == "decode":
        new_position = position - shift
    generated_text += alphabet[new_position]
  print(f"The {direction}d text is {generated_text}")

answer = "yes"
while answer == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction, text, shift)
  answer = input("Do you want to try again? Type 'yes' or 'no'.\n")
