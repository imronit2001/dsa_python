"""BinarySearchTree.py"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    # Function to insert a newNode
    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            curNode = self.root
            parentNode = None
            while curNode is not None:
                parentNode = curNode
                if data < curNode.data:
                    curNode = curNode.left
                else:
                    curNode = curNode.right

            if data < parentNode.data:
                parentNode.left = newNode
            else:
                parentNode.right = newNode
