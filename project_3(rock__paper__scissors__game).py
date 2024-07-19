import random

options = ("rock", "paper", "scissors")
running_1 = True

while running_1:

    player_1 = None
    computer_1 = random.choice(options)

    while player_1 not in options:
        player_1 = input("Enter a choice (rock, paper, scissors): ")

    print(f"User : {player_1}")
    print(f"Computer : {computer_1}")

    if player_1 == computer_1:
        print("It's a tie")
    elif player_1 == "rock" and computer_1 == "scissors":
        print("You win")
    elif player_1 == "paper" and computer_1 == "rock":
        print("You win")
    elif player_1 == "scissors" and computer_1 == "paper":
        print("You win")
    else:
        print("You lose")

    if not input("press once more if you want to play again ?: ").lower() == "once more":
        running_1 = False

print("Thanks for playing")