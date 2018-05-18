# palindrome.py
from MyQueue import Queue
from Stack import Stack
import string

#------------------------------------------------------------

def isPalindrome(phrase): 
    forward = Queue()
    reverse = Stack()
    extractLetters(phrase, forward, reverse)
    return sameSequence(forward, reverse)

#------------------------------------------------------------

'''pre: ch is alpha characters only
   post: encodes ch to queue and pushes ch to stack'''

def extractLetters(phrase, q, s):
    for ch in phrase:
        if ch.isalpha():
            ch = ch.lower()
            q.enqueue(ch)
            s.push(ch)

#------------------------------------------------------------

'''pre: q.size() is bigger than 0
   post: compares first character in queue and last character in stack
         if all are equal then return true'''

def sameSequence(q, s):

    if q.size() > 0: #checks if q.size() is bigger than 0
        ch1 = q.dequeue() # ch1 equals the first character in queue
        ch2 = s.pop() #ch2 equals the last character in stack
        
        if ch1 != ch2: #if ch1 not equal ch2 then return false
            return False

        sameSequence(q, s) #calls sameSequence for the remaining characters
                           #in both queue and stack
    return True


print(isPalindrome("race car"))
print(isPalindrome("Hello"))
print(isPalindrome("A man, a plan, a canal, Panama!"))
