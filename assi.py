print("hello")
import random

# Game choices
choices = ["snake", "water", "gun"]

print("Welcome to Snake, Water, Gun Game!")

player_score = 0
computer_score = 0

while True:

    player = input(
        "\nEnter snake, water, gun or quit: "
    ).lower().strip()

    if player == "quit":
        break

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Your choice:", player)
    print("Computer choice:", computer)

    if player == computer:
        print("It's a Draw!")

    elif (
        (player == "snake" and computer == "water")
        or (player == "water" and computer == "gun")
        or (player == "gun" and computer == "snake")
    ):
        print("Congratulations! You Win!")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("Your Score:", player_score)
    print("Computer Score:", computer_score)

print("\nGame Over!")
print("Final Score:")
print("Your Score:", player_score)
print("Computer Score:", computer_score)

if player_score > computer_score:
    print("You won the game!")
elif computer_score > player_score:
    print("Computer won the game!")
else:
    print("The game ended in a draw!")

    """⭐ Important Rules Yaad Rakho
Combination	Winner
Snake vs Water	Snake 🐍
Water vs Gun	Water 💧
Gun vs Snake	Gun 🔫
Same choices	Draw 🤝"""