class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DDL:
    def __init__(self):
        self.head =None
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head==None:
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp =temp.next
        temp.next = new_node
        new_node.prev = temp
    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp =temp.next
            
    def push(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        new_node.next =self.head
        self.head.prev = new_node
        self.head =new_node
        
    def insertAfter(self,prev,data):
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node
        new_node.next.prev = new_node
        new_node.prev = prev
    
    def insertBefore(self,next_node,data):
        new_node = Node(data)
        new_node.prev = next_node.prev
        next_node.prev.next = new_node
        new_node.next = next_node
        next_node.prev = new_node
    
    def deleteNode(self,key):
        temp = self.head
        if temp.data == key:
            self.head = temp.next
            self.head.prev = None
            return
        while(temp):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp.next.prev = prev
    
    def arrayToList(self,array):
        for elements in array:
            self.append(elements)
            
    def listToArray(self):
        array = []
        temp = self.head
        while(temp):
            array.append(temp.data)
            temp = temp.next
        return array
    
    def reverseList(self):
        prev = None
        head = self.head
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        self.head = prev

    def getMiddleElement(self):
        
        a = self.head
        b = self.head
        
        while a and a.next:
            b = b.next
            a = a.next.next
            
        print("\nThe Middle Element is ",b.data)
        
        
ddl = DDL()
ddl.append(1)
ddl.append(2)
ddl.append(3)
ddl.append(4)
ddl.push(0)
ddl.insertAfter(ddl.head,0)
ddl.insertAfter(ddl.head.next,1)
ddl.deleteNode(0)
ddl.deleteNode(1)
ddl.printlist()
print("\nArray to list")
elements = [5,6,7,8]
ddl.arrayToList(elements)
ddl.printlist()
print("\nList To Array")
sad = ddl.listToArray()
print(sad)
print("\nReverse List")
ddl.reverseList()
ddl.printlist()
ddl.getMiddleElement()



        
        