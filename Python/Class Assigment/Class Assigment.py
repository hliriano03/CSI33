class ListNode(object):

    def __init__(self, item = None, link = None):

        self.item = item
        self.link = link

    def __str__(self):

        return str(self.item)


def print_list(node):

    if node == None: # it means that there are no more nodes in the list
        print("No more elements in the list")
    else: # more elements are available
        print(node.item,"\t",end="")
        print_list(node.link)
    
n5 = ListNode(5)
n3 = ListNode(3, n5)
n7 = ListNode(7, n3)
n25 = ListNode(25, n7)

##n30 = ListNode(30, n3.link)
##n3.link = n30

n25.link = n7.link


