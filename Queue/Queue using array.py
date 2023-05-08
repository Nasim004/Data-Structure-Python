

class Queue:

    def __init__(self):
        self.queue = [None]*5
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        self.rear = self.rear + 1
        self.queue[self.rear] = data

    def dequeue(self):
        self.front = self.front + 1

    def display(self):
        for i in range(self.front+1, self.rear+1):
            print(self.queue[i])


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print('******')
q.dequeue()
q.display()
