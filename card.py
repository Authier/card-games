class Card():
    def __init__(self, value: str, suit: str=None, description: str=None) -> None:
        if (not isinstance(value, str)) or (not isinstance(suit, (str, None))) or (not isinstance(description, (str, None))):
            raise TypeError("check type")
        self.value = value
        self.suit = suit
        self.description = description
        return None