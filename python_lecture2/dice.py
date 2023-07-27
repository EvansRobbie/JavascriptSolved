import random
class Roll:
    def __init__(self, dice_number):
        self.dice_number = dice_number
    def dice(self):
        for i in range(2):
            choice = random.choice(self.dice_number)
            print(list(choice))


# dice_numbers = [1, 2, 3, 4, 5, 6]
# roll = Roll(dice_numbers)
# roll.dice()