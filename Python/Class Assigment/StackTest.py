# 725+*367-*-

# 3 - 2 * (5 + (7 - 3))

import sys
import unittest

from Stack import *

# Stack.py
class StackTest(unittest.TestCase):

    #------------------------------------------------------------

    def testPush(self):
        
        '''post: places x on top of the stack'''

        stack = Stack()
        stack.push(5)
        
        self.assertEqual(stack.items[-1],5)

    #------------------------------------------------------------

    def TestPop(self):

        '''post: removes and returns the top element of 
        the stack'''

        stack = Stack()
        stack.push(5)
        stack.pop(5)
        
        self.assertEqual(stack.items[-1],0)

    #------------------------------------------------------------

    def top(self):

        '''post: returns the top element of the stack without 
        removing it'''

        return self.items[-1]

    #------------------------------------------------------------

    def size(self):

        '''post: returns the number of elements in the stack'''

        return len(self.items)

def main(argv):
  unittest.main()

if __name__ == '__main__':
  main(sys.argv)
