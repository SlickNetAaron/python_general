from random import randint
from sys import exit

def get_input():
    num_dice_input = input("How many dice do you want to roll? [1-6] ").strip()
    return num_dice_input

def parse_input(user_input):
    if user_input.isnumeric():
        dice_count = int(user_input)
        if dice_count in range(1,7):
            return dice_count
    print("Please enter a valid number 1-6")
    exit()

def roll_dice(count):
    dice_list = []
    for dice in range(0, count):
        dice_list.append(randint(1,6))
    return dice_list

def main():
    while True:
        user_input = get_input()
        num_dice = parse_input(user_input)
        dice_values = roll_dice(num_dice)
        print(*dice_values)

if __name__ == "__main__":
    main()
