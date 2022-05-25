
####
# This version is built on my own
# I don't think I care about displaying the ascii text and will probably skip that
####

from random import randint

def parse_input(input_string):
    input_string = input_string.strip()
    if input_string == None or user_input == "x":
        SystemExit(1)
    if input_string in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Invalid entry. Enter a valid number of dice, 1-6")
        SystemExit(1)

def generate_dice_rolls(num_dice):
    dice_list = []
    for dice in range(0, num_dice):
        dice_list.append(randint(1,6))
    return dice_list
    
while True:
    user_input = input("How many dice do you want to roll? [1-6] ")
    parse_input(user_input)
    selection = parse_input(user_input)
    dice_values = generate_dice_rolls(selection)
    print(dice_values)
    
