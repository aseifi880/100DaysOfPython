
import random
import os
from ascii_art import hangman_stages, hangman_art


##############################
# reversed so it corresponds with 'lives' index
# with 0 lives it prints zeroth index of reversed hangman_stages
hangman_stages.reverse()
##############################

print(hangman_art)

word_list = ["adult", "advertise", "advise", "affect"]
chosen_word = random.choice(word_list)
display = ['-' for i in chosen_word]

lives = 6
game_over = False

while not game_over:
    print(hangman_stages[lives])
    print(' '.join(display))
    player_letter = input("Guess a letter: ")
    os.system('cls')
    #if the guessed letter is not in the word player
    #losed one life
    #when 'lives' is 0 the man is hanged and player loses
    if player_letter not in chosen_word:
            lives -= 1
            print(f"You guessed wrong! {player_letter} is not in the word!")
            if lives == 0:
                print(hangman_stages[0])
                print("You lose!")
                game_over = True
    else:
        #if a letter was formerly guesse no lives are lost
        if player_letter in display:
             print(f'You already guessed {player_letter}')
        else:
            for index in range(len(chosen_word)):
                if player_letter == chosen_word[index]:
                    display[index] = player_letter
        
    if '-' not in display:
        print("You won!")
        game_over = True
    
