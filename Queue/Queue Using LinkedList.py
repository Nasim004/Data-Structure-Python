class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        newnode = Node(data)
        if self.rear is None:
            self.front = newnode
            self.rear  = newnode
            
        else:
            self.rear.next = newnode
            self.rear = newnode
            
    def dequeue(self):
        if self.front is None:
            print("empty")
        else:
            self.front=self.front.next
            
    def display(self):
        if self.front is None:
            print("Queue Empty")
            return
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next
            
queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.dequeue()
queue.display()


