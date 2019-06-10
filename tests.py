from cards import *
from thisgame import *

def test_discard(game):
    game.discard_round()
    for discard in game.discard_pile:
        if discard is not 'cards.Card':
            print("card object not discarded")
        else:
            print("test_discard: passed")

def main():
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
    hand_size = 4
    deck.move_cards(player1.hand, hand_size)
    deck.move_cards(player2.hand, hand_size)
    deck.move_cards(player3.hand, hand_size)
    # test discard round
    test_discard(game)

main()
