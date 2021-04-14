# Caesar Cipher - Encrpytion

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    output = ""
    if direction == "decode":
        shift *= -1
    for let in text:
        if let in alphabet:
            position = alphabet.index(let)
            new_position = position + shift
            new_let = alphabet[new_position]
            output += new_let
        else:
            output += let
            
    print(f"The {direction}d message is {output}")
    
    

from art import logo
print(logo)

should_end = False        

while not should_end:
    
    direction = input("Type 'encode' to encrpyt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift %= 26
    
    caesar(text, shift, direction)
    
    restart = input("Do you want to restart the cipher program? 'Yes' or 'No'?\n")
    
    if restart.lower() == "no":
        should_end = True
        print("Goodbye")

