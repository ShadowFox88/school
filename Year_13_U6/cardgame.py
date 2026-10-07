class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
        self.__a = "a"
        self._b = "b"

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

deck = [
    Card(suit, name) for suit in ["Clubs", "Diamonds", "Hearts", "Spades"] 
    for name in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
]

print(deck[0]._Card__a)


