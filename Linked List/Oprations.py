class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):

        new_node = Node(new_data)
        if self.head is None:
            self.head = Node(new_data)

        else:

            temp = self.head

            while (temp.next):

                temp = temp.next

            temp.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, target):
        temp = self.head
        if temp == target:
            temp = self.head.next
            self.head = temp
            return
        while (temp):
            if temp.data == target:
                break
            prev = temp
            temp = temp.next
            prev.next = temp.next

    def array_to_lists(self, arr):
        for i in arr:
            self.append(i)

    def list_to_array(self):
        temp = self.head
        array = []
        while (temp):
            array.append(temp.data)
            temp = temp.next
        return array

    def printMiddleElement(self):
        a = self.head
        b = self.head

        while a and b:
            b = b.next
            a = a.next.next

        return (b.data)


list = Linked_list()
list.append(1)
list.push(0)
list.append(2)
list.append(3)
list.append(4)
list.deleteNode(1)
list.insertAfter(list.head, 0)
list.printList()
arr = [0, 0, 0]
print("\n")
list.array_to_lists(arr)
list.printList()
print("\n")
l = list.list_to_array()
print(l)
print("\n")
m = list.printMiddleElement()
print(m)
