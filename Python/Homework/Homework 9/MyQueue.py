#!/usr/bin/env python
# Queue.py
# Dave Reed
# CS161
# 02/24/2006

#----------------------------------------------------------------------

class Queue:

    #----------------------------------------------------------------------
    
    def __init__(self):

        '''create an empty FIFO queue'''
        
        self.q = []

    #----------------------------------------------------------------------

    def size(self):

        '''return number of items in the queue

        pre: none
        
        post: returns number of items in the queue'''
        
        return len(self.q)

    #----------------------------------------------------------------------

    def enqueue(self, x):

        '''insert x at end of queue

        pre: none

        post: x is added to the queue'''
        
        self.q.append(x)

    #----------------------------------------------------------------------

    def front(self):

        '''return first item in queue

        pre: queue is not empty; IndexError is raised if empty

        post: returns first item in the queue'''

        return self.q[0]

    #----------------------------------------------------------------------

    def dequeue(self):

        '''remove and return first item in queue

        pre: queue is not empty; IndexError is raised if empty

        post: removes and returns first item in the queue'''
        
        return self.q.pop(0)

    #----------------------------------------------------------------------

    def queueInOrder(self):

        '''remove and return first item in queue

        pre: queue is not empty

        post: copies all enqueues into two separete list, originalQueue, and orderdedQueue.
              orderedQueue gets ordered and gets compared to originalQueue, if they are the same
              then returns True, if not then returns False'''

        if self.size() > 0: #checks that SomeQueue is not empty

            originalQueue = [] #creates empty list
            orderedQueue = [] #creates empty list
            
            for item in range(self.size()): #goes through every item in queue

                originalQueue.append(self.dequeue()) #dequeues them into originalQueue

            for item in originalQueue: #goes through every item in originalQueue list

                self.enqueue(item) #copies them back to queue
                orderedQueue.append(item) #copies them to ordedQueue list

            for i in range(len(orderedQueue)): #goes through every item in orderedQueue

                Min = i #assigns the minimum to current number

                for a in range(i+1, len(orderedQueue)): #goes through every item in orderedQueue starting with the next position
                    
                    if orderedQueue[a] < orderedQueue[Min]: #compares next position with current min to see which one is smaller

                        Min = a #if next position is smaller, then current minimum becomes that position

                temp = orderedQueue[Min] #creates a temporary variable copying current minimum position
                orderedQueue[Min] = orderedQueue[i] #swaps current minimum position with i position
                orderedQueue[i] = temp #swaps i position to temp position, which is current minimum position
                    
            if originalQueue == orderedQueue: #if originalQueue equals orderedQueue then return true
                return True

            else: #if not then return false
                return False

    def combine(self, q1, q2):

        combinedq = []

        for i in range(q1.size()):

            combinedq.append(q1.dequeue())

        for i in range(q2.size()):

            combinedq.append(q2.dequeue())   

        combinedq = sorted(combinedq)

        for i in combinedq:

            self.enqueue(i)

        return self.q

        

            


Q1 = Queue()
Q1.enqueue(1)
Q1.enqueue(3)
Q1.enqueue(7)
Q1.enqueue(14)
Q1.enqueue(16)
Q1.enqueue(18)
Q1.enqueue(20)
Q1.enqueue(55)


Q2 = Queue()
Q2.enqueue(5)
Q2.enqueue(10)
Q2.enqueue(12)
Q2.enqueue(25)
Q2.enqueue(28)
Q2.enqueue(35)
Q2.enqueue(60)

Q3 = Queue()
print(Q3.combine(Q1,Q2))
