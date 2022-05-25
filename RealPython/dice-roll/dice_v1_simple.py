from random import randint

num_dice_input = input("How many dice do you want to roll? [1-6] ")

if num_dice_input.strip() in {"1", "2", "3", "4", "5", "6"}:
    num_dice = int(num_dice_input.strip())
    dice_list = []
    for dice in range(0, num_dice):
        dice_list.append(randint(1,6))
    
for dice in dice_list:
    print(dice)
