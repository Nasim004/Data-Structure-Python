class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Empty")
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


newstack = Stack()
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
