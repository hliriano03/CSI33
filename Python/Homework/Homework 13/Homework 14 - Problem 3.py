def preOrder(self, root, List = []):
        
        """post: Returns a pre-ordered traversal"""

        if root is not None and root.item is not None:

            List.append(root.item)
            self.preOrder(root.left, List)
            self.preOrder(root.right, List)

        return List

def postOrder(self, root, List = []):
        
        """post: Returns a post-ordered traversal"""
        
        if root is not None and root.item is not None:
            
            self.postOrder(root.left, List)
            self.postOrder(root.right, List)
            List.append(root.item)

        return List
