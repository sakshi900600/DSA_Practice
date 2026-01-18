# insertAthead , deleteNode, get, put


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    

class LRU:
    def __init(self, cap):
        self.cap = cap
        self.dct = {}
        self.head = Node(-1)
        self.tail = Node(-1)

    
    def insertAtHead(self, node):
        


