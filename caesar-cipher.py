alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift, direction):
  end_text = ""
  if direction == "decode":
    shift *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift
      end_text += alphabet[new_position]
    
  print(f"Here's the {direction}d result: {end_text}")
  
  
from art import logo

print(logo)

cont = True

while cont:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  
  caesar(start_text = text, shift = shift, direction = direction)
  
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
  
  if restart == "no":
    cont = False  
    print("Goodbye.")
