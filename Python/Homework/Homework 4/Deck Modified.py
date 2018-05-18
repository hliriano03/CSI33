# Deck.py

from random import randrange
from random import shuffle
from Card import Card
  
class Deck(object):

    #------------------------------------------------------------

    def __init__(self):

        """post: Creates a 52 card deck in standard order"""

        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank,suit))
        self.cards = cards
        self.decksize = len(self.cards) # creates an instance variable to keep
                                        # track of desksize

    #------------------------------------------------------------

    def size(self):

        """Cards left
        post: Returns the number of cards in self"""
        
        return len(self.cards)

    #------------------------------------------------------------

    def deal(self):

        """Deal a single card
        pre:  self.size() > 0
        post: Returns the next card, and removes it from self.card if
        the deck is not empty, otherwise returns False"""

        if self.size() > 0:
            self.decksize = self.size() - 1 # this does not affect the run-time
                                            # efficiency of the size() operation
            return self.cards.pop()
        else:
            return False

    #------------------------------------------------------------

    def shuffle(self):

        """Shuffles the deck
        post: randomizes the order of cards in self"""

        n = self.size()
        cards = self.cards
        shuffle(cards) #shuffle imported from random makes the suffle more effective
                       #and faster

    #------------------------------------------------------------

    def addTop(self, card):

        """Adds Card to top of deck
        post: sets a card on top of desk"""
        self.cards.insert(0, card)

    #------------------------------------------------------------

    def addBottom(self, card):

        """Adds Card to bottom of deck
        post: sets a card at bottom of desk"""

        self.cards.insert(len(self.cards)+1, card) # gets the last position of
                                                   # cards

    #------------------------------------------------------------

    def addRandom(self, card):

        """Adds Card to random position in deck
        post: sets a card in a random position in desk"""

        pos = randrange(0, len(self.cards)) # gets a random number from 0 to
                                            # the amount of cards in deck

        self.cards.insert(pos, card)

            
