import random
import os

while True:
    os.system('cls')
    print("Welcome to Rock Paper Scissor!\n")
    print("What do you choose? rock, paper or scissors?\n")
    choice_list = ['rock', 'paper', 'scissors']

    user_choice = input()
    print('You Chose:\n')
    if user_choice == 'rock':
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
    elif user_choice == 'paper':
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
    elif user_choice == 'scissors':
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
        
    machine_choice = random.choice(choice_list)
    print('Machine Chose:\n')
    if machine_choice == 'rock':
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
    elif machine_choice == 'paper':
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
    elif machine_choice == 'scissors':
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)

    if machine_choice == user_choice:
        print("Noway, It's a Draw 🥲")
    elif (machine_choice == 'rock' and user_choice == 'paper') or (machine_choice == 'paper' and user_choice == 'scissors') or (machine_choice == 'scissors' and user_choice == 'rock'):
        print("WOW! You won!╰(*°▽°*)╯")
    elif (machine_choice == 'paper' and user_choice == 'rock') or (machine_choice == 'rock' and user_choice == 'scissors') or (machine_choice == 'scissors' and user_choice == 'paper'):
        print('Aww, You lose 😭')

    input("Press enter to reset.")