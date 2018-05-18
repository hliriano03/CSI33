# Bridge.py

from Player import Player
from Deck import Deck
from Card import Card
from random import randint

class Bridge(object):

    """Starts the game of Bridge"""

    #------------------------------------------------------------

    def __init__(self, player1, player2):

        """post: Creates players and all the other game components"""

        self.P1 = Player(player1)
        self.P1.pile = []
        self.P2 = Player(player2)
        self.P2.pile = []
        self.deck = Deck()

        #shuffles desk 5 times
        for shuffle in range(5):

            self.deck.shuffle()

        self.trumpSuit = Card.suitName(self.deck.cards[randint(1,52)])

    #------------------------------------------------------------


    def pickCard(self):

        """post: Picks a card from deck and displays them for both players"""

        #adds a card to player 1's hand from the desk
        self.P1.addCard(self.deck.deal())
        print(self.P1.getName(), "picked the", self.P1.hand.cards[-1])
        #adds a card to player 2's hand from the desk
        self.P2.addCard(self.deck.deal())
        print(self.P2.getName(), "picked the", self.P2.hand.cards[-1])

    def run(self):
        
        """ pre: creates a hand for each player and checks that theres cards
                 in the desk
            post: prints out the round results, checks if any of the players
            have a trump card, if both have card with same suit then who ever
            has the highest value of the card wins the game, if non have a trump
            card, then the game is a tie, and if one have a trump card and the
            other one doesnt then that player with the trump card wins the round."""

        count = 0

        print("\n===========[Trump Card]===========\n")
        print("*" + str(self.trumpSuit) + "*\n")

        #creates a empty hand for each player
        self.P1.createHand()
        self.P2.createHand()

        #game continues until theres no cards left
        while self.deck.size() != 0:

            
            print("=============[Round " + str(count+1) + "]=============\n")
    
            self.pickCard()

            #checks if player 1 card picked is not a trump card
            if self.P1.hand.cards[-1].suitName() != self.trumpSuit:

                #checks if player 2 card picked is not a trump card
                if self.P2.hand.cards[-1].suitName() != self.trumpSuit:

                    #checks if both players have a card with same suit
                    if self.P1.hand.cards[-1].suitName() == self.P2.hand.cards[-1].suitName():

                        #checks if player 2 card has a higher value and wins
                        if self.P1.hand.cards[-1] <= self.P2.hand.cards[-1]:

                            print("\n*" + str(self.P2.getName()), "Won Round*")
                            print("Adding Cards to " + str(self.P2.getName()) + "'s pile\n")
                            self.P2.pile.append(self.P1.hand.cards.pop())
                            self.P2.pile.append(self.P2.hand.cards.pop())

                        #if not then player 1 card has a higher value and wins
                        else:
                            print("\n*" + str(self.P1.getName()), "Won Round*")
                            print("Adding Cards to " + str(self.P1.getName()) + "'s pile\n")
                            self.P1.pile.append(self.P1.hand.cards.pop())
                            self.P1.pile.append(self.P2.hand.cards.pop())

                    #if false then game is tied and both card are disgarded
                    else:
                        print("\n*Tied Game*\n")
                        self.P1.hand.cards.pop()
                        self.P2.hand.cards.pop()
                        continue

                #if player 2 has a trump card then player 2 wins
                #and adds both cards to his/her pile
                else:
                    print("\n*" + str(self.P2.getName()), "Won Round*")
                    print("Adding Cards to " + str(self.P2.getName()) + "'s pile\n")
                    self.P2.pile.append(self.P1.hand.cards.pop())
                    self.P2.pile.append(self.P2.hand.cards.pop())

            #if non of the previous checks apply then that means player 1 has
            #the trump card
            else:
                #checks if player 2 does not have a trump card if player 2 doesnt have one then player 1 wins
                if self.P2.hand.cards[-1].suitName() != self.trumpSuit:
                    print("\n*" + str(self.P1.getName()), "Won Round*")
                    print("Adding Cards to " + str(self.P1.getName()) + "'s pile\n")
                    self.P1.pile.append(self.P1.hand.cards.pop())
                    self.P1.pile.append(self.P2.hand.cards.pop())

                #else if player 2 has a trump card then check who has a higher value
                else:
                    #checks if player 2 card has a higher value
                    if self.P1.hand.cards[-1] <= self.P2.hand.cards[-1]:

                        print("\n*" + str(self.P2.getName()), "Won Round*")
                        print("Adding Cards to " + str(self.P2.getName()) + "'s pile\n")
                        self.P2.pile.append(self.P1.hand.cards.pop())
                        self.P2.pile.append(self.P2.hand.cards.pop())

                    #if not then player 1 card has a higher value
                    else:
                        print("\n*" + str(self.P1.getName()), "Won Round*")
                        print("Adding Cards to " + str(self.P1.getName()) + "'s pile\n")
                        self.P1.pile.append(self.P1.hand.cards.pop())
                        self.P1.pile.append(self.P2.hand.cards.pop())
                    

            count += 1

        #prints the results of the game
        print("=============End of Game=============\n")

        print(str(self.P1.getName()) + "'s Pile Has " + str(len(self.P1.pile)) + " Cards")
        print(str(self.P2.getName()) + "'s Pile Has " + str(len(self.P2.pile)) + " Cards")

        if len(self.P1.pile) == len(self.P2.pile):

            print("\nIt's a Tied Game")

        elif len(self.P1.pile) > len(self.P2.pile):

            print("\n" + str(self.P1.getName()), "Won Game with " + str(len(self.P1.pile)) + " Cards in the Pile")

        else:
            print("\n" + str(self.P2.getName()), "Won Game with " + str(len(self.P2.pile)) + " Cards in the Pile")

B = Bridge("Player 1", "Player 2")
B.run()
