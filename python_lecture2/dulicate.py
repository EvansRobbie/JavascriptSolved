# numbers = [1, 2, 2, 3, 4, 5,6]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)
from dice import Roll

dice_numbers = [1, 2, 3, 4, 5, 6]
roll = Roll(dice_numbers)

roll.dice()

# Roll.dice(dice_numbers)
