from typing import Tuple, List
from random import randint
from card import Card
from abc import ABC, abstractmethod


class DefaultDeck(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.deck = []
        return None


    def get_cards(self, number_of_cards: int) -> List[Card]:
        if len(self.deck) < number_of_cards:
            raise IndexError("not enough cards in deck")
        cards = []
        while number_of_cards != 0:
            card = self.deck.pop()
            cards.append(card)
            number_of_cards -= 1
        return cards


    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("card not of correct type")
        self.deck.append(card)
        return None


    def shuffle(self) -> None:
        if len(self.deck) <= 1:
            return None
        for _ in range(len(self.deck) * 10):
            idx1, idx2 = self.__get_two_rand_indexes()
            self.deck[idx1], self.deck[idx2] = self.deck[idx2], self.deck[idx1]
        return None


    def show_cards(self, simple: bool=True) -> List[str]:
        output = []
        for card in self.deck:
            string = self.__card_to_string(card, simple)           
            output.append(string)
        return output


    def __get_two_rand_indexes(self) -> Tuple[int, int]:
        rand_idx_1 = randint(0, len(self.deck) - 1)
        rand_idx_2 = randint(0, len(self.deck) - 1)
        return (rand_idx_1, rand_idx_2)


    def __card_to_string(self, card: Card, simple_view: bool) -> str:
        if not isinstance(card, Card):
            raise TypeError("card not of correct type")
        temp_string = card.value
        if (card.suit is not None) and (not simple_view):
            temp_string += f' - {card.suit}'
        if (card.description is not None) and (not simple_view):
            temp_string += f' - {card.description}'
        return temp_string


class Standard52CardDeck(DefaultDeck):
    def __init__(self) -> None:
        self.deck = []
        for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for value in ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                card = Card(f'{value[0] if len(value) > 2 else value} {suit}', suit, f'{value} of {suit}')
                self.deck.append(card)
        return None


class Standard52CardDeckJokers(DefaultDeck):
    def __init__(self) -> None:
        self.deck = [Card("Joker", "Red", "Red Joker"), Card("Joker", "Black", "Black Joker")]
        for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for value in ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                card = Card(f'{value[0] if len(value) > 2 else value} {suit}', suit, f'{value} of {suit}')
                self.deck.append(card)
        return None


class CatanResourceDeck(DefaultDeck):
    def __init__(self) -> None:
        self.deck = []
        for _ in range(19):
            self.deck.append(Card("Ore", "Resource", ""))
            self.deck.append(Card("Grain", "Resource", ""))
            self.deck.append(Card("Lumber", "Resource", ""))
            self.deck.append(Card("Wool", "Resource", ""))
            self.deck.append(Card("Brick", "Resource", ""))
        return None