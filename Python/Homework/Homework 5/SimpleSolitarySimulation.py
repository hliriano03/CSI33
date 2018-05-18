# SimpleSolitary.py

from SimpleSolitary import SimpleSolitary

class SimpleSolitarySimulation(object):

    #------------------------------------------------------------

    def __init__(self, games, dealtcards):

        self.games = games
        self.dealtcards = dealtcards
        self.wins = 0
        self.loses = 0

    #------------------------------------------------------------

    def run(self):

        """runs simulation
        post: runs simulation, with dealtcards and prints out the wins and loses."""

        for game in range(self.games): #runs x amount of games

            C = SimpleSolitary(self.dealtcards)
            C.run() #runs simulation

            if C.isGameWon == True: #if the game is won then it adds 1 to self.wins
                self.wins += 1

            else:
                self.loses += 1 #if the game is won then it adds 1 to self.wins

        print(self) #prints results

    def __str__(self):

        return str("Wins: ") + str(self.wins) + str(" Loses: ") + str(self.loses)


S = SimpleSolitarySimulation(40,5) #simulates 40 games with 5 dealt cards
S.run()

S = SimpleSolitarySimulation(40,6) #simulates 40 games with 6 dealt cards
S.run()

S = SimpleSolitarySimulation(40,7) #simulates 40 games with 7 dealt cards
S.run()

S = SimpleSolitarySimulation(40,8) #simulates 40 games with 8 dealt cards
S.run()

