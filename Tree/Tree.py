class Tree:
    def __init__(self,data):

        self.data = data 
        self.children = []

    def add_Node(self,node):
        self.children.append(node)

    def delete_child(self,data):
        for i , child in enumerate(self.children):
            if child.data == data:
                del self.children[i]
                return
            else:
                child.delete_child(data)
                


