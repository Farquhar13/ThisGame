import random

class Card:
    """
    Represents a standard playing card
    Attributes:
        rank: 0-14
        suit: 0-3
    """
    rank_names = ["None", "Ace/One", "2", "3", "4", "5", '6',
            '7', '8', '9', "10", "Jack", "Queen", "King", "Ace"]
    suit_names = ["Club", "Diamond", "Heart", "Spade"]
    
    def __init__(self, rank=0, suit=0):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return '%s of %ss'% (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    
    # check if two objects are the same with ==
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # is same suit (2 cards)
    def suited(self, other):
        return self.suit == other.suit

class Deck:
    """
    Represents a standard deck
    Attributes:
        cards: a list of cards
    """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(2,15):
                new_card = Card(rank, suit)
                self.cards.append(new_card)

    def __str__(self):
        res = []
        for i, card in enumerate(self.cards):
            res.append(str(i+1)+ ': ' +str(card))
        return '\n'.join(res)

    def shuffle(self):
        """Shuffles the cards in the deck"""
        random.shuffle(self.cards)

    def add_card(self, card):
        """Add a card to the deck"""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck"""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns card from the deck
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())

    def sort(self):
        """Sorts cards in ascending order"""
        sorted_hand = []
        for suit in Card.suit_names:
            suited_cards = []
            suited_ranks = []
            for card in self.cards:
                if Card.suit_names[card.suit] == suit:
                   suited_cards.append(card)
                   suited_ranks.append(card.rank)

            indices = list(range(len(suited_cards)))

            if indices:
                indices.sort(key=suited_ranks.__getitem__)
                # loop trhough indices reordering
                for i in indices:
                   sorted_hand.append(suited_cards[i]) 
        sorted_hand.reverse() # Not sure if this makes it more or less reabable
        self.cards = sorted_hand
           
class Hand(Deck):
    """ Represents a hand of playing cards
    Attributes:
        - cards: (list) empty by default
        - label: (string) name for the player or some identification of whose hand it is
    """

    def __init__(self, label=''):
        self.cards = []
        self.label = label

if __name__ == '__main__':
    deck = Deck()
    hand = Hand("player one")
    deck.shuffle()
    deck.move_cards(hand, 5)
    print(hand)
    print()
    hand.sort()
    print(hand) 

