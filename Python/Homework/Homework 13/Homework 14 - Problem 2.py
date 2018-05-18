def find_rec(self, root, item):
        
    """ Search for item in BST
        post: Returns item from BST if found, None otherwise"""
    
    if root is not None and not(root.item == item):

        if item < root.item:
            return self.find(root.left, item)
        else:
            return self.find(root.right, item)

    else:
        try:
            return root.item

        except AttributeError:
            print('None')

B = BST()
B.insert(10)
B.insert(7)
B.insert(13)
B.insert(54)
B.insert(1)
B.insert(3)
