# BST.py
from TreeNode import TreeNode

class BST(object):

    #------------------------------------------------------------

    def __init__(self):
        
        """create empty binary search tree
        post: empty tree created"""

        self.root = None

    #------------------------------------------------------------

    def insert(self, item):

        """insert item into binary search tree
        pre: item is not in self
        post: item has been added to self"""

        if self.root is None:   # handle empty tree case
            self.root = TreeNode(item)
        else:
            # start at root
            node = self.root
            # loop to find the correct spot (break to exit)
            while True:
                if item == node.item:
                    raise ValueError("Inserting duplicate item")

                if item < node.item:           # item goes in left subtree
                    if node.left is not None:  # follow existing subtree
                        node = node.left
                    else:                      # empty subtree, insert here
                        node.left = TreeNode(item)
                        break
                else:                          # item goes in right subtree
                    if node.right is not None: # follow existing subtree
                        node = node.right
                    else:                      # empty subtree, insert here
                        node.right = TreeNode(item)
                        break

    #------------------------------------------------------------

    def __len__(self):

        """insert item into binary search tree
        pre: item is not in self
        post: item has been added to self"""

        return len(self.asList())

    #------------------------------------------------------------

    def insert_rec(self, item):

        """insert item into binary search tree
        pre: item is not in self
        post: item has been added to self"""

        self.root = self._subtreeInsert(self.root, item)

    #------------------------------------------------------------

    def _subtreeInsert(self, root, item):

        if root is None:          # inserting into empty tree
            return TreeNode(item) # the item becomes the new tree root

        if item == root.item:
            raise ValueError("Inserting duplicate item")

        if item < root.item:                              # modify left subtree
            root.left = self._subtreeInsert(root.left, item)
        else:                                             # modify right subtree 
            root.right = self._subtreeInsert(root.right, item)

        return root # original root is root of modified tree

    #------------------------------------------------------------

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

    #------------------------------------------------------------

    def find(self, root, item):
        
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
        
    #------------------------------------------------------------

    def preOrder(self, root, List = []):
        
        """post: Returns a pre-ordered traversal"""
        
        if root is not None and root.item is not None:

            List.append(root.item)
            self.preOrder(root.left, List)
            self.preOrder(root.right, List)

        return List

    #------------------------------------------------------------

    def postOrder(self, root, List = []):
        
        """post: Returns a post-ordered traversal"""
        
        if root is not None and root.item is not None:
            
            self.postOrder(root.left, List)
            self.postOrder(root.right, List)
            List.append(root.item)

        return List

    #------------------------------------------------------------

    def delete(self, item):

        """remove item from binary search tree
        post: item is removed from the tree"""
        
        self.root = self._subtreeDelete(self.root, item)

    #------------------------------------------------------------

    def _subtreeDelete(self, root, item):

        if root is None:   # Empty tree, nothing to do
           return None
        if item < root.item:                             # modify left
            root.left = self._subtreeDelete(root.left, item)
        elif item > root.item:                           # modify right
            root.right = self._subtreeDelete(root.right, item)
        else:                                            # delete root
            if root.left is None:                        # promote right subtree
                root =  root.right
            elif root.right is None:                     # promote left subtree
                root = root.left
            else:
                # root node can't be deleted, overwrite it with max of 
                #    left subtree and delete max node from the subtree
                root.item, root.left = self._subtreeDelMax(root.left)
        return root

    #------------------------------------------------------------

    def _subtreeDelMax(self, root):
        
        if root.right is None:           # root is the max 
            return root.item, root.left  # return max and promote left subtree
        else:
            # max is in right subtree, recursively find and delete it
            maxVal, root.right = self._subtreeDelMax(root.right)
            return maxVal, root  

    #------------------------------------------------------------

    def asList(self):

        """gets item in in-order traversal order
        post: returns list of items in tree in orders"""
        
        items = []
        self._subtreeAddItems(self.root, items)
        return items

    #------------------------------------------------------------

    def _subtreeAddItems(self, root, itemList):
        if root is not None:
            self._subtreeAddItems(root.left, itemList)
            itemList.append(root.item)
            self._subtreeAddItems(root.right, itemList)

    #------------------------------------------------------------

    def visit(self, f):

        """perform an in-order traversal of the tree
        post: calls f with each TreeNode item in an in-order traversal
        order"""
        
        self._inorderVisit(self.root, f)

    #------------------------------------------------------------

    def _inorderVisit(self, root, f):
        
        if root is not None:
            self._inorderVisit(root.left, f)
            f(root.item)
            self._inorderVisit(root.right, f)

    #------------------------------------------------------------

    def __iter__(self):

        """in-order iterator for binary search tree"""
        
        return self._inorderGen(self.root)

    #------------------------------------------------------------

    def _inorderGen(self, root):
        
        if root is not None:
            # yield all the items in the left subtree
            for item in self._inorderGen(root.left):
                yield item
            yield root.item
            # yield all the items from the right subtree
            for item in self._inorderGen(root.right):
                yield item

    #------------------------------------------------------------

