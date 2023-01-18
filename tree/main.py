from main import *

class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.add(data, self.root)

    def add(self, data, node):
        if data < node.data:
            if node.left:
                self.add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.add(data, node.right)
            else:
                node.right= Node(data)

    def printin(self, node):
        if not (node.left and node.right):
            print(node.data)
        if node.left:
            self.printin(node.left)
            print(node.data)
        if node.right:
            self.printin(node.right)

    def printpre(self, node):
        print(node.data)
        if node.left:
            self.printpre(node.left)
        if node.right:
            self.printpre(node.right)

    def printpost(self, node):
        if node.left:
            self.printpost(node.left)
        if node.right:
            self.printpost(node.right)
        print(node.data)

    def inorder(self): # Left, Root, Right 
        if self.root:
            self.printin(self.root)
        else:
            print("No data")

    def preorder(self): # Root, Left, Right
        if self.root:
            self.printpre(self.root)
        else:
            print("No data")

    def postorder(self): # Left, Right, Root
        if self.root:
            self.printpost(self.root)
        else:
            print("No data")

    def insertOrder(self, data):
        pass