from cards import *
import numpy as np

# global variations
hand_size = 4

class Player():
    """ Representation of a player
    Attributes:
        - name: Name of the player
        - chips: (list) with 
    """
    def __init__(self, name='', score=0):
        self.name = name
        self.chips = ["Blue", "White", "Green", "Red", "Black"]
        self.hand = Hand(self.name)
        self.score = score

    # what member functions do I want?
    # discard card
    def discard(self, i=-1):
       return self.hand.pop_card(i)
       
class Game():
    def __init__(self, players=[]):
        self.players = players
        self.void_cards = [] # for past discards and "blacked" cards
        self.discard_pile = []
        self.add_disc_pile  = [] 

    def discard_round(self):
        # players enter the discard round
        for player in self.players:
            print(player.name, "discard")
            print(player.hand)
            while True: # loop for user validation
                card_id = input("Enter the card to discard: ")
                if card_id == '':
                    continue
                # bounds checking
                card_id = int(card_id) - 1 
                if card_id < 0 or card_id > (len(player.hand.cards) - 1):
                    print("Invalid discard id")
                else:
                    self.discard_pile.append(player.discard(card_id))
                    break

    def additional_discard(self, disc_players):
        # almost the same as discard_round for now, just with fewer players and
        # additional discards go into different game "pile"
        for player in self.players:
            print(player.name, "discard")
            print(player.hand)
            while True: # loop for user validation
                card_id = input("Enter the card to discard: ")
                if card_id == '':
                    continue
                # bounds checking
                card_id = int(card_id) - 1 
                if card_id < 0 or card_id > (len(player.hand.cards) - 1):
                    print("Invalid discard id")
                else:
                    self.add_disc_pile.append(player.discard(card_id))
                    break
      
    # change to game.order with players appended
    # seems like I really need a argsort based on rank
    def turn_order(self, discarded=self.discard_pile):
        # get card ranks
        ranks = []
        for card in discarded: 
            ranks.append(card.rank)
        print(ranks)
        # get order indices
        turn_idx = []
        for r in ranks:
            # case where same rank discarded by multiple players
            min_rank = min(ranks)
            if rank.count(min_rank) > 1:
                # players discard again
                player_idx = np.where(ranks == min_rank)
                disc_players = self.players(player_idx) 
                self.additional_discard(disc_players)
                
                
                
            min_index = ranks.index(min(ranks))
            turn_idx.append(min_index)
            ranks[min_index] = max(ranks) + 1 # avoid reselection
        print("index", turn_idx)
        

if __name__ == '__main__':
    # start the game
    game = Game()
    # get a the deck
    deck = Deck()
    deck.shuffle()
    # set the players
    player1 = Player("Eugene")
    player2 = Player("Willis")
    player3 = Player("Carol")
    game.players = [player1, player2, player3]
    # get hands
    deck.move_cards(player1.hand, hand_size)
    deck.move_cards(player2.hand, hand_size)
    deck.move_cards(player3.hand, hand_size)
    # discard round
    game.discard_round()
    # determine highest discard for turn order
    # add discarded thing to players class, add function for card rank
    # evalutaion, determine order 


    print("\ntesting zone")
    game.turn_order() 
