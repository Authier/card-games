from __future__ import annotations
from typing import Tuple, List, Optional
from random import randint
from decks import DefaultDeck, Standard52CardDeck, Standard52CardDeckJokers, CatanResourceDeck
from card import Card
from player import Player
from abc import ABC, abstractmethod

class DefaultCardGame(ABC):
    @abstractmethod
    def __init__(self, players: List[Player]=[]) -> None:
        """
        This will show all the players that are at the table and initialize that.
        """
        self.players = ["DEALER", ]

    def remove_player(self, player: Player) -> bool:
        pass

    def __refresh_deck(self) -> None:
        pass


class BlackJackGame(DefaultCardGame):
    def __init__(self, players: List[Player] = []) -> None:
        super().__init__(players)
    
p1 = Player("JACOB")
p2 = Player("GEORGE")
x = BlackJackGame([p1, p2])
print(x.players)