import random

def roll_dice():
#roll the dice
    return random.randint(1, 6)

def play_round(roll1, roll2):
#Rolls random variables and prints different outputs depending on the results
    print(f"Player 1 rolls a {roll1}, Player 2 rolls a {roll2}.", end=' ')
    if roll1 > roll2:
        print("Player 1 wins the round.")
        return 1
    elif roll2 > roll1:
        print("Player 2 wins the round.")
        return 2
    else:
        print("The round is a tie.")
        return 0

def main():
#Asks how many rounds the player watns to play
    try:
        rounds = int(input("How many rounds do you want to play? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    player1_wins = 0
    player2_wins = 0
    ties = 0
#keeps track of the score
    for i in range(1, rounds + 1):
        roll1 = roll_dice()
        roll2 = roll_dice()
        result = play_round(roll1, roll2)

        if result == 1:
            player1_wins += 1
        elif result == 2:
            player2_wins += 1
        else:
            ties += 1
#prints final score
    print(f"\nFinal Score: Player 1 wins {player1_wins} round(s). Player 2 wins {player2_wins} round(s). {ties} round(s) ended in a tie.")
#shows the winner
    if player1_wins > player2_wins:
        print("Overall Winner: Player 1!")
    elif player2_wins > player1_wins:
        print("Overall Winner: Player 2!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    main()