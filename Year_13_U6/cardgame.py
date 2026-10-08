import random


class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __repr__(self):
        return f"{self.suit} {self.name}"

    @property
    def value(self):
        return int(self.name) if self.name.isnumeric() else {
            "Queen": 10,
            "King": 10,
            "Jack": 10,
            "Ace": 11,
        }[self.name]

    @property
    def is_ace(self):
        return self.name == "Ace"

def is_bust(cards):
    value = sum([i.value for i in cards])
    aces = sum(1 if i.is_ace else 0 for i in cards)

    return value - (aces * 10) > 21

deck = [
    Card(suit, name) for suit in ["Clubs", "Diamonds", "Hearts", "Spades"] 
    for name in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
]

random.shuffle(deck)

