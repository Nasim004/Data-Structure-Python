


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self,new_data):
        new_node = Node(new_data)
        if self.head==None:
            self.head = new_node
            return
        last = self.head    
        while(last.next):
            last =last.next
        last.next = new_node

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end="")
            temp = temp.next
    
    def insertAfter(self,prev_node,new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def deleteNode(self,key):
        temp = self.head
        if temp.data == key:
            temp = self.head.next
            self.head = temp
            return
        while (temp):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            prev.next = temp.next
            
    def arrayToList(self,array):
        for i in array:
            self.append(i)
            
    def getLength(self):
        
        temp =self.head
        count = 0
        while (temp is not None):
            count = count + 1
            temp = temp.next
        print("\nThe length of list :",count)
    def listToArray(self):
        arr = []
        temp = self.head
        while (temp is not None):
            arr.append(temp.data)
            temp = temp.next
        return arr
    def printMiddleElement(self):
        a = self.head
        b = self.head

        while a and a.next:
            b = b.next
            a = a.next.next
            
        return (b.data)
    
            
    
    
    
    
    
    
    

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
print("List before deletion")
llist.printList()
print("\nList After Push")
llist.push(0)
llist.printList()
print("\nAfter inserting in between")
llist.insertAfter(llist.head.next,0)
llist.printList()
print("\nAfter deleting a node")
llist.deleteNode(1)
llist.printList()
print("\nArray to list")
i = [5,6,7,8]
llist.arrayToList(i)
llist.printList()
llist.getLength()
print("\nLinkedList To Array")
s=llist.listToArray()
print(s)
llist.printList()
llist.printMiddleElement()


