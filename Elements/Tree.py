class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print (self.data)
        if self.right is not None:
            self.right.inorder()

    def preorder(self):
        print (self.data)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print (self.data)
        
