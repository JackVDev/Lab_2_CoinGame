"""
    player.py
    Jack Verdin
    This program holds the player class, and all variables and methods relating to it.
    06/27/2026
"""

from coin import Coin

class Player:
    """
        The player class, which holds information about a specific player in the game.
        Attributes: __name:string, __wallet:int=20, __mycoin:Coin()
    """

    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__mycoin = Coin()