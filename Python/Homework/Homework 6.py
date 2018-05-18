# ListNode2.py

class ListNode2(object):
    
    def __init__(self, item = None, leftL = None, rightL = None):

        '''creates a ListNode with the specified data value and
           two links: to the previous node and to the next node
        post: creates a ListNode with the specified data value and links'''
        
        # put the code here
        self.item = item
        self.leftL = leftL
        self.rightL = rightL

    def __str__(self):
      ''' for printing the node '''
      
      return str(self.item)

def printLR(headNode):
    """ prints all elements following right links, starting with the headNode """
    node = headNode
    
    while node is not None:
        print(node.item, end = "\t")
        node = node.rightL

    print("end of linked list")

def printRL(tailNode):
    """ generates a list all elements following left links,
    starting with the tailNode """
    
    node = tailNode
    listV = []
    
    while node is not None:
        listV.append(node.item)
        node = node.leftL
    
    listV = listV[::-1]
    print("here is the list of elements, following left links:",listV)

    return listV

#create linked list

n5 = ListNode2(10)
n4 = ListNode2(7,None,n5)

n5.leftL = n4

n3 = ListNode2(23,None,n4)

n4.leftL = n3

n2 = ListNode2(1,None,n3)

n3.leftL = n2

n1 = ListNode2(34,None,n2)

n2.leftL = n1

# printing all the nodes, one by one, following right links, then left links

print("\nDisplaying List\n")
printLR(n1)
print("\r")
printRL(n5)
print("\r")

# Then insert new value, say 8 between 34 and 1. Display the updated list

print("Inserting 8...")

n6 = ListNode2(8,n1,n2)
n1.rightL = n6
n2.leftL = n6

print("\r")
printLR(n1)
print("\r")
printRL(n5)
print("\r")

# Then delete node with value 7, update the links and display the new list.

print("Deleting 7...")

n5.leftL = n3
n3.rightL = n5
del(n4)

print("\r")
printLR(n1)
print("\r")
printRL(n5)
print("\r")

