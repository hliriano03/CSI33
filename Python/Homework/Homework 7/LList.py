# LList.py
from ListNode import ListNode

class LList:

    #------------------------------------------------------------

    def __init__(self, seq=()):

        """create an LList
        post: creates a list containing items in seq"""
     
        if seq == ():
            # No items to put in, create an empty list
            self.head = None
            self.tail = None
        else:
            # Create a node for the first item
            self.head = ListNode(seq[0], None)
            self.tail = ListNode(seq[-1], None)

            # Add remaining items keeping track of last node added
            self.tail = self.head
            for item in seq[1:]:
                self.tail.link = ListNode(item, None)
                self.tail = self.tail.link

        self.size = len(seq)
   
    #------------------------------------------------------------

    def __len__(self):

        '''post: returns number of items in the list'''

        return self.size

    #------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list'''
        
        assert 0 <= position < self.size

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link
        return node

    #------------------------------------------------------------

    def append(self, x):

        '''appends x onto end of the list
        post: x is appended onto the end of the list'''

        # create a new node containing x
        newNode = ListNode(x)

        # link it into the end of the list
        if self.head is not None:
            # non-empty list
            self.tail.link = newNode
            self.tail = newNode
        else:
            # empty list
            # set self.head to new node
            self.head = newNode
        self.size += 1

    #------------------------------------------------------------

    def __getitem__(self, position):

        '''return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position'''

        node = self._find(position)
        return node.item
    
    #------------------------------------------------------------

    def __setitem__(self, position, value):

        '''set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value'''

        node = self._find(position)
        node.item = value

    #------------------------------------------------------------

    def __delitem__(self, position):

        '''delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from 
        the list'''

        assert 0 <= position < self.size

        self._delete(position)

    #------------------------------------------------------------

    def _delete(self, position):

        #private method to delete item at location position from the list
        # pre: 0 <= position < self.size
        # post: the item at the specified position is removed from the list
        # and the item is returned (for use with pop)

        if position == 0:
            # save item from the initial node
            item = self.head.item

            # change self.head to point "over" the deleted node
            self.head = self.head.link

        else:
            # find the node immediately before the one to delete
            prev_node = self._find(position - 1)

            # save the item from node to delete
            item = prev_node.link.item

            # change predecessor to point "over" the deleted node
            prev_node.link = prev_node.link.link

        self.size -= 1
        return item

    #------------------------------------------------------------

    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item

        pre: self.size > 0 and ((i is None or (0 <= i < self.size))

        post: if i is None, the last item in the list is removed
        and returned; otherwise the item at position i is removed 
        and returned'''

        assert self.size > 0 and (i is None or (0 <= i < self.size))

        # default is to delete last item
        # i could be zero so need to compare to None
        if i is None:
            i = self.size - 1
        
        return self._delete(i)

    #------------------------------------------------------------

    def insert(self, i, x):

        '''inserts x at position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list at position i and 
              old elements from position i..oldsize-1 are at positions 
              i+1..newsize-1'''

        assert 0 <= i <= self.size

        if i == 0:
            # insert before position 0 requires updating self.head
            self.head = ListNode(x, self.head)
        else:
            # find item that node is to be insert after
            node = self._find(i - 1)
            node.link = ListNode(x, node.link)
        self.size += 1

    #------------------------------------------------------------

    def __copy__(self):
    
        '''post: returns a new LList object that is a shallow copy of self'''
        
        a = LList()
        node = self.head
        while node is not None:
            a.append(node.item)
            node = node.link
        return a

    #------------------------------------------------------------

    
##     def __iter__(self):

##         # generator version works in both Python2 and Python3
##         node = self.head
##         while node is not None:
##             yield node.item
##             node = node.link


    #------------------------------------------------------------

        def __iter__(self):

            return LListIterator(self.head)
    
    #------------------------------------------------------------

    def __min__(self):

        '''post: returns the lower value of the list'''

        Min = self._find(len(L)-1).item
        
        for i in range(len(self)):
            if Min == 0:
                Min = self._find(i).item

            if self._find(i).item < Min:
                Min = self.find(i).item

        return Min
    
    #------------------------------------------------------------

    def __max__(self):

        '''post: returns biggest value of the list'''

        Max = self._find(len(L)-1).item
        
        for i in range(len(self)):
            if self._find(i).item > Max:
                Max = self._find(i).item

        return Max


    #------------------------------------------------------------

    def index(self, x):

        '''post: returns the position of the x of the list'''
        
        try:
            for i in range(len(self)):
                if self._find(i).item == x:
                    return i

            raise ValueError
        
        except ValueError:
            return str(x) + str(" is not in linked list")


    #------------------------------------------------------------

    def count(self, x):

        '''post: returns the x amount of times x is in list'''
        
        count = 0

        for i in range(len(self)):
            if self._find(i).item == x:
                count += 1

        return count
    
    #------------------------------------------------------------

    def remove(self, x):

        '''post: removes x from list'''

        for i in range(len(self)):
            if self._find(i).item == x:

                return self.__delitem__(i)


            
    #------------------------------------------------------------

    def reverse(self):

##         # create a new node containing x
##        newNode = ListNode(x)
##
##        # link it into the end of the list
##        if self.head is not None:
##            # non-empty list
##            self.tail.link = newNode
##            self.tail = newNode
##        else:
##            # empty list
##            # set self.head to new node
##            self.head = newNode
##        self.size += 1

        '''post: removes x from list'''

        tempList = LList()

        for i in range(self.size):

            newNode = ListNode(self._find(self.size - (i + 1)).item)

            if tempList.head is not None:
                # non-empty list
                tempList.tail.link = newNode
                tempList.tail = newNode
            else:
                # empty list
                # set self.head to new node
                tempList.head = newNode
                tempList.tail = newNode
            tempList.size += 1

        self.head = tempList.head

#------------------------------------------------------------

class LListIterator:

    #------------------------------------------------------------

    def __init__(self, head):
        self.currnode = head

    #------------------------------------------------------------
    # Python2 version
    def next(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item

    #------------------------------------------------------------
    # Python3 version
    def __next__(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item

L = LList([10,1,13,7,3])

##L.reverse()
##print("the reversed list: ")
##for item in L:
##    print(item, end=" ")
