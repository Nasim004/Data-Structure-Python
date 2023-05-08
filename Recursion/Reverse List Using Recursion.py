class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            
    def reverseList(self,temp):
        if temp is None or temp.next is None:
            return temp
        reverse = self.reverseList(temp.next)
        temp.next.next = temp
        temp.next = None
        return reverse
            
            
            
list = LinkedList()
list.push(10)
list.push(20)
list.push(30)
list.push(40)
list.printList()
print("\n")
list.head=list.reverseList(list.head)
list.printList()


