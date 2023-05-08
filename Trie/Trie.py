class Trienode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self,word):
        current = self.root
        for c in word:
            if c  not in current.children:
                current.children[c] = Trienode()
            current = current.children[c]
        current.end = True

    def search(self,word):
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.end 


t = Trie()

t.insert('apple')
t.insert('monkey')
print(t.search('abcd'))

