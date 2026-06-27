"""
    Lab9_JackVDev-1.py
    Jack Verdin
    This is the main program for the Lab 9 coding activity.
    06/27/2026
"""
from player import Player

def main():
    #Run program
    print("- Coin Matching Game -")
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    gameover = False
    while not(gameover):
        # Flip coins and print the sides
        # Check for matching sides, if match p1 wins, else p2 wins
        # Display coins remaining
        # Loop exit conditions: user input, either player has 0 coins
        if player1.get_wallet() < 1 or player2.get_wallet() < 1:
            gameover = True
        elif input("Do you want to toss the coins? (y/n): ").lower() != "y":
            gameover = True

if __name__ == "__main__":
    main()