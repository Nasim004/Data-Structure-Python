class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
        
    def push(self,data):
        newnode = Node(data)
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
    
    def pop(self):
        if self.top is None:
            print("Under Flow")
            return
        self.top = self.top.next
        
    def display(self):
        if self.top is None:
            print("Stack Empty")
            return
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next
            
newstack = stack()
print("Before POP")
newstack.push(1)
newstack.push(2)
newstack.push(3)
newstack.push(4)
newstack.push(5)
newstack.display()

print("After POP")
newstack.pop()
newstack.pop()


newstack.display()