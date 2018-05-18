# Player.py

from Hand import Hand

class Player(object):

    """A labeled collection of cards that can be sorted"""

    #------------------------------------------------------------

    def __init__(self, Name):

        """Creates player"""

        self.player = Name

    #------------------------------------------------------------

    def getName(self):
        
        """ Add card to the hand """

        return self.player

    def createHand(self):

        self.hand = Hand(self.player)

    def addCard(self,card):

        self.hand.add(card)

    def dumpCard(self):

        self.hand.dump()
