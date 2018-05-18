# SimpleSolitary.py

from random import randint
from Card import Card
from Deck import Deck
  
class SimpleSolitary(object):

    #------------------------------------------------------------

    def __init__(self, DealtCards):

        """post: Creates a 52 card deck in standard order then shuffles it
                 finally it puts down DealtCards face up"""

        self.deck = Deck()
        self.dealtcards = []
        self.isGameWon = False

        self.deck.shuffle()

        for n in range(DealtCards):

            self.dealtcards.append(self.deck.deal())

    #------------------------------------------------------------

    def run(self):

        """runs game
        pre:  self.deck.size() not equal 0
        post: Compares each card's rank to check if theres any matches, if there
              is then for each matching card a new card is put on top of it
              face up, if there another match then the same happens. Player wins
              if there is no more cards in deck. Player loses if there are no
              matching cards while there are cards in deck."""

        while self.deck.size() != 0:

            position = [] #creates a list to keep record of matching cards

            for card1 in self.dealtcards:

                for card2 in self.dealtcards: #for each card it checks for the
                                              #other cards

                    if card1 == card2: #makes sure the card is not the same
                        continue
                    
                    if card1.rank() == card2.rank(): #if card's rank is equal to
                                                     #the second card's rank then
                                                     #we can replace both

                        position.append(tuple((self.dealtcards.index(card1),card1.rank()))) #creates a tuple of both card's position and card's rank

##            for card in self.dealtcards: #prints all card that are face up
##                print(card)

##            print("\r")
            
            if len(position) != 0: #checks that there are matching cards

                for p in position:

                    self.dealtcards[p[0]] = self.deck.deal()


            else: #if not then game over
##                print("Game over, no matching cards to replace.\n")
                break

        if self.deck.size() == 0: #once done if checks again if there is any cards left
                                  #if not then game is won
##            print("Game Finished, No more cards on Deck. You Win!.\n")
            self.isGameWon = True

##S = SimpleSolitary(6)
##S.run()
