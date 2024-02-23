import math, string
alphabet = list(string.ascii_lowercase)
def caesar_cipher(text : str, shift_number : int, direction :str):
    out_text = ""
    if direction == "decode":
        shift_number *= -1
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (shift_number + pos) % 26
            out_text += alphabet[new_pos]
        else:
            out_text += char
    print(f'The output text is : {out_text}')

input_text = input("What's your text? ")
shift_num = int(input("Your number of shifts? "))
dir = input("Enter 'decode' or 'encode': ")

caesar_cipher(input_text, shift_num, dir)