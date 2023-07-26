import random

my_game = ["Rock", "Paper", "Scissors"]
computer = random.choice(my_game)

player = None
while player not in my_game:
    player = input("Rock, Paper or Scissors?").lower()
    # print("Wrong choice")
if player == computer:
    print("computer", computer)
    print('player', player)
    print('Tie')
elif player == "Rock":
    if computer == "Paper":
        print("computer", computer)
        print('player', player)
        print('You win')
    if computer == "Scissors":
        print("computer", computer)
        print('player', player)
        print('You Lose')
elif player == "Paper":
    if computer == "rock":
        print("computer", computer)
        print('player', player)
        print('You win')
    if computer == "Scissors":
        print("computer", computer)
        print('player', player)
        print('You Lose')
elif player == "Scissors":
    if computer == "Paper":
        print("computer", computer)
        print('player', player)
        print('You win')
    if computer == "rock":
        print("computer", computer)
        print('player', player)
        print('You Lose')