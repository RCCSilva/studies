import enum

class CardType(enum.Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

class CardNumber(enum.Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NICE = 9
    TEN = 10
    QUEEN = 11
    KING = 12
    JACK = 13

class Card:
    def __init__(self, type: CardType, number: CardNumber):
        self.type = type
        self.number = number