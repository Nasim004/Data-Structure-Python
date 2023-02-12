class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
            
    def inOrder(self,root):
        res = []
        if root:
            res = self.inOrder(root.left)
            res.append(root.data)
            res = res +self.inOrder(root.right)
        return res
    
    def preOrder(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res
    
    def postOrder(self,root):
        res = []
        if root:
            res = self.postOrder(root.right)
            res = res + self.postOrder(root.left)
            res.append(root.data)
        return res
    
    
    
    
    def findval(self,x):
        if x < self.data:
            if self.left is None:
                return str(x)+" Not Found"
            return self.left.findval(x)
        
        elif x > self.data:
            if self.right is None:
                return str(x)+" Not Found"
            return self.right.findval(x)
        else:
            print(str(self.data)+" Found")
    
    
    def delete(self,x):
        
        if self.data is None:
            print("No elements in tree")
            
        if x < self.data:
            if self.left:
                self.left.delete(x)
            else:
                print("No such element")
                
        elif x > self.data:
            if self.right:
                self.right.delete(x)
            else:
                print("No such element")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.self.left:
                node = node.self.left
            self.data = node.data
            self.left = self.left.delete(node.data)
        return self
    
    
    
    
    
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data,end=" "),
        if self.right:
            self.right.printtree()

tree = Node(100)

tree.insert(99)
tree.insert(98)
tree.insert(97)
tree.insert(96)
tree.insert(95)

tree.insert(101)
tree.insert(102)
tree.insert(103)
tree.insert(104)
tree.insert(105)



print("Before Traversal")
tree.printtree()

print("\nAfter Inorder")
print(tree.inOrder(tree))

print("\nAfter PreOrder")
print(tree.preOrder(tree))

print("\nAfter PostOder")
print(tree.postOrder(tree))

print("\n")    
print(tree.findval(100))
    