"""
    coin.py
    Jack Verdin
    This program holds the coin class, and all variables and methods relating to it.
    06/27/2026
"""

from random import choice

class Coin:
    """
        The coin class, holds a private attribute __sideup which can be randomized with toss() and read with get_sideup()
    """

    def __init__(self):
        # Initializes the class and randomizes __sideup
        self.__sideup = choice(["Heads", "Tails"])

    def toss(self):
        # Randomizes __sideup between "Heads" and "Tails"
        self.__sideup = choice(["Heads", "Tails"])

    def get_sideup(self):
        return self.__sideup