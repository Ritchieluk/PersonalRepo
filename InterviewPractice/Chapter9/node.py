class Node:

    def __init__(self, value=None, left_node=None, right_node=None):
        self.data=value
        self.left=left_node
        self.right=right_node

    def setValue(self, value):
        self.data = value

    def getValue(self):
        return self.data
    
    def traverse(self):
        print('Preorder: %d' % self.data)
        if self.left:
            self.left.traverse()
        print('Inorder: %d' % self.data)
        if self.right:
            self.right.traverse()
        print('Postorder: %d' % self.data)
    
