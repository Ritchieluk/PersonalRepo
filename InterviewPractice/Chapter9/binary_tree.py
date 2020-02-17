from node import Node
from typing import List
import random
Vector = List[float]

class Binary_Tree:
    root = None
    def __init__(self, input_array: Vector):
        self.root = Node(input_array[0])
        for data in input_array[1:]:
            self.insert(data)

    def insert(self, data):
        node = self.root
        if not node.left:
            node.left = Node(data)
            return
        if not node.right:
            node.right = Node(data)
            return
        while(node.left or node.right):
            if not node.left:
                node.left = Node(data)
                return
            elif not node.right:
                node.right = Node(data)
                return
            else:
                roll = random.randint(1,100)
                node = node.left if roll <= 50 else node.right
        node.left = Node(data)

    def printTree(self):
        if self.root:
            self.root.traverse()

    def getDepth(self, node=None, currDepth=0):
        if not node:
            node = self.root
        leftDepth = currDepth
        rightDepth = currDepth
        if node.left:
            leftDepth = self.getDepth(node.left, currDepth+1)
        if node.right:
            rightDepth = self.getDepth(node.right, currDepth+1)
        return leftDepth if leftDepth >= rightDepth else rightDepth