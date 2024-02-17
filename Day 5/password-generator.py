import random
import string

letters = string.ascii_letters
digits = string.digits
syms = "!#$&+*()%"

print("Welcome to the 'Random Password Generator'.")
num_letters = int(input("How many letters do you want in you password? "))
num_digits = int(input("How many digits do you want in you password? "))
num_syms = int(input("How many symbols do you want in you password? "))
password_letter = random.sample(letters, num_letters)
password_digits = random.sample(digits, num_digits)
password_syms = random.sample(syms, num_syms)
password_in_order = password_letter + password_digits + password_syms
random.shuffle(password_in_order)
password = ''.join(password_in_order)
print("Your password is: " + password)