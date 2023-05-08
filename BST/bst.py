class BST:
    def __init__(self, data):
        self.root = data
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.root is None:
            self.root = data
            return

        if self.root == data:
            return
        if self.root > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)

        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def find(self, x):
        if self.root is None:
            print("No elements in tree")
        if self.root == x:
            print("Node is Found")
            return
        if x < self.root:
            if self.lchild:
                self.lchild.find(x)
            else:
                print("Node Not Found")

        elif x > self.root:
            if self.rchild:
                self.rchild.find(x)
            else:
                print(" Node Not Found")

        else:
            print("Found")

    def preOrder(self):
        print(self.root)
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.root)

    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.root)
        if self.rchild:
            self.rchild.inOrder()

    def secondLargest(self):
        c = [0]
        second_largest(self.root, c)

    def second_largest(self, root, c):          
        if root is None or c[0] >= 2:
            return
        secondLargest(root.right, c)
        c[0] += 1
        if c[0] == 2:
            print("Second largest", root.data)
            return
        secondLargest(root.left, c)


tree = BST(10)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(11)
tree.insert(12)
tree.insert(13)

tree.find(18)

# tree.min_node()
tree.secondLargest()
