#Final Project - Project 1

from turtle import *
import math

class Kochizing(Turtle):

    def __init__(self):

        """pre: Initiates Turtle and sets settings"""

        Turtle.__init__(self) #Initites Turtle
        self.pensize(2) #changes the size of the line to 2
        self.speed(-1) #speeds up the drawing process, the less the number the faster
        self.ht() #hides cursor

        self.length = 0 #assigns a temp value to self.length
        self.degree = 0 #assings a temp value to self.degree

        self.isDrawCCurve = False #a check for when is C Curve will be drawn
        self.isDrawSnowFlake = False #a check from when is Snow Flake will be drawn

    def DrawCCurve(self, length, degree):

        """pre: Both length and degree are integer, length is not 0 and degree is not less than 0
           post: Sets isDrawSnowFlake to False, and isDrawCCurve to True, then calls the drawing function"""

        if (type(length) == int and length is not 0) and \
           (type(degree) == int and degree >= 0):
            
            self.length = length #assings length to self.length
            self.degree = degree #assings degree to self.degree
            
            self.clear() #clears any existing drawings
            self.penup() #stops drawing even if turtle is moving
            self.goto(150,100) #goes to (x,y) coordiation in canvas)
            self.pendown() #starts drawing
            
            self.isDrawSnowFlake = False #sets isDrawSnowFlake to False to prevent issues with drawing C Curve
            self.isDrawCCurve = True #sets isDrawCCurve to True
            
            self._draw(self.length, self.degree) #Calls private function ._draw() with given length and degree

        else:
            raise Exception("length cannot be 0, and degree cannot be less than 0") #raises exception if length is not an integer or equal to 0 and if degree not an integer or less than 0

    def DrawSnowFlake(self, length, degree):

        """pre: Both length and degree are integer, length is not 0 and degree is not less than 0
           post: Sets isDrawSnowFlake to False, and isDrawCCurve to True, then calls the drawing function"""

        if (type(length) == int and length is not 0) and \
           (type(degree) == int and degree >= 0):
            
            self.length = length
            self.degree = degree
            
            self.clear()
            self.penup()
            self.goto(-300,100)
            self.pendown()
            
            self.isDrawCCurve = False #sets isDrawCCurve to False to prevent issues with drawing SnowFlake
            self.isDrawSnowFlake = True

            runs = 3

            while runs != 0: #creates the snowflake by running 3 times turning it 120 degrees after each drawing
                self._draw(self.length, self.degree) #Calls private function ._draw() with given length and degree
                self.right(120) #Turns right 120 degrees
                runs -= 1 #substracts 1 to runs

        else:
            raise Exception("length cannot be 0, and degree cannot be less than 0")

    def _draw(self,length, degree):

        """pre: Need to have a a length and a degree and checks whether isDrawCCurve is True or isDrawSnowFlake is True
           post: Draws C Curve or SnowFlake depending on which is True"""

        if self.isDrawCCurve is True: #checks if its drawing a C Curve
            
            if degree == 0: #if the degree is 0 then draw a straight line with same length
                self.forward(length)

            else:
                self.left(45) #turn left 45 degrees
                self._draw(length/math.sqrt(2),degree-1) #Calls Koch function again with one degree less
                self.right(90) #turns right 90 degrees
                self._draw(length/math.sqrt(2),degree-1) #Calls Koch function again with one degree less
                self.left(45) #turns left 45 degrees

        elif self.isDrawSnowFlake is True: #checks if its drawing a SnowFlake

            
            if degree == 0: #if the degree is 0 then draw a straight line with same length
                self.forward(length)

            else:
                self._draw(length/math.sqrt(2),degree-1) #Calls private function ._draw() again with one degree less
                self.left(60) #turn left 60 degrees
                self._draw(length/math.sqrt(2),degree-1)
                self.right(120) #turns right 120 degrees
                self._draw(length/math.sqrt(2),degree-1)
                self.left(60) #turns left 60 degrees
                self._draw(length/math.sqrt(2),degree-1)

        
        else:
            raise Exception("Cannot call this function directly") #raises an error in case this function gets called directly instead of other functions calling it

K = Kochizing()
K.DrawCCurve(-300,12)

