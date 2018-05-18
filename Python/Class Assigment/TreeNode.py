# TreeNode.py
class TreeNode(object):

    def __init__(self, data = None, left=None, right=None):
    
        """creates a tree node with specified data and references to left 
        and right children"""
    
        self.item = data
        self.left = left
        self.right = right

def preOrder(tree, L):

    if tree is not None:

        L.append(tree.item)
        preOrder(tree.left, L)
        preOrder(tree.right, L)

    return L

def inOrder(tree, L):

    if tree is not None:

        inOrder(tree.left, L)
        L.append(tree.item)
        inOrder(tree.right, L)

    return L

def postOrder(tree, L):

    if tree is not None:

        postOrder(tree.left, L)
        postOrder(tree.right, L)
        L.append(tree.item)

    return L        

root = TreeNode(10,TreeNode(6,TreeNode(3,None,TreeNode(5,TreeNode(4))),TreeNode(8,TreeNode(7))),TreeNode(15,TreeNode(12,TreeNode(11)),TreeNode(17,TreeNode(16))))


