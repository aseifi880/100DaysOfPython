print(
    '''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 
'''
)

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
first_choice = input("You're at a crossroads. Where do you want to go? Type 'left' or 'right'.\n")
if first_choice == "right":
    print('You fell into a  pithole. Game Over!')
elif first_choice == "left":
    second_choice = input("You arrived at a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or type 'swim' to swim across.\n")
    if second_choice == "swim":
        print('You became food for fish. Game Over!')
    elif second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose?\n")
        if third_choice == "red":
            print('The house exploded. Game Over!')
        elif third_choice == "blue":
            print('The door knob was charged. You got electrified!')
        elif third_choice == "yellow":
            print('You find a mountain of treasures, You won!')
