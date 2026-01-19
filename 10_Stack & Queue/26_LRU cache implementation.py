# insertAthead , deleteNode, get, put


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    

class LRU:
    def __init__(self, cap):
        self.cap = cap
        self.dct = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    
    def insertAtHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def delete(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    

    def get(self, key):
        if key not in self.dct:
            return -1
        
        node = self.dct[key]
        val = node.value
        self.delete(node)
        self.insertAtHead(node)
        return val
    
    def put(self, key, val):
        if key in self.dct:
            node = self.dct[key]
            node.value = val
            self.delete(node)
            self.insertAtHead(node)
        else:
            if len(self.dct) == self.cap:
                node = self.tail.prev
                self.delete(node)
                del self.dct[node.key]
            
            newNode = Node(key, val)
            self.dct[key] = newNode
            self.insertAtHead(newNode)
        



if __name__ == "__main__":
    sol = LRU(2)
    sol.put(1, 1)
    sol.put(2, 2)
    print(sol.get(1))    # return 1
    sol.put(3, 3)        # evicts key 2
    print(sol.get(2))    # return -1 (not found)
    sol.put(4, 4)        # evicts key 1
    print(sol.get(1))    # return -1 (not found)
    print(sol.get(3))    # return 3
    print(sol.get(4))    # return 4

        




