import random


class Card:
    VALUES = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value < other.value
        
        return NotImplemented
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._deck = [Card(rank, suit)
                              for suit in Deck.SUITS 
                              for rank in Deck.RANKS]
        random.shuffle(self._deck)

    def draw(self):
        if not self._deck:
            self.__init__()
        return self._deck.pop()
        
        

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]

    def print(self):
       for card in self._hand:
           print(f"{card}")

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        min_value = 10
        for card in self._hand:
            if card.value < 10:
                min_value = card.value
        
        return min_value == 10 and self._is_straight_flush()

    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self):
        return self._is_n_of_a_kind(4)

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        suit = self._hand[0].suit
        for card in self._hand:
            if card.suit != suit:
                return False
        
        return True

    def _is_straight(self):
        sorted_cards = sorted([card.value for card in self._hand])

        card_sequence = [value 
                         for value in range(sorted_cards[0], sorted_cards[0] + 5)]
        return sorted_cards == card_sequence

    def _is_three_of_a_kind(self):
        return self._is_n_of_a_kind(3)

    def _is_two_pair(self):
        rank_counts = {}
        for card in self._hand:
            rank_counts[card.rank] = (rank_counts.get(card.rank, 0) + 1)
        
        pairs = {_: value for _, value in rank_counts.items() if value == 2}

        return len(pairs) == 2

    def _is_pair(self):
        return self._is_n_of_a_kind(2)

    def _is_n_of_a_kind(self, number):
        rank_counts = {}
        for card in self._hand:
            rank_counts[card.rank] = (rank_counts.get(card.rank, 0) + 1)
        
        matches = [1 for count in rank_counts.values() if count == number]

        return len(matches) == 1



hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")