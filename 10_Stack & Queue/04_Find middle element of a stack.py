class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        self.mid = None

    
    def push(self, x):
        newNode = Node(x)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.mid = newNode
            self.length = 1
            return
        
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

        self.length += 1
        if self.length % 2 == 0:
            self.mid = self.mid.next


    def pop(self):
        if self.head == None:
            return self.head

        data = self.tail.data
        self.tail.prev.next = None
        self.tail = self.tail.prev

        self.length -= 1
        if self.length %2 != 0:
            self.mid = self.mid.prev
        
        return data
    

    def findMid(self):
        return self.mid.data
    
    def deleteMid(self):
        if self.mid == None:
            return
        
        prevNode = self.mid.prev
        nextNode = self.mid.next

        if prevNode != None:
            prevNode.next = nextNode
        if nextNode != None:
            nextNode.prev = newNode



if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    print(st.findMid(), end=" ")
    # print(st.pop())




# gfg code : --------------------------
class Solution2:
    def deleteMid(self, stack):
        #code here
        n = len(stack)
        
        if n%2 == 0:
            mid = (n//2) -1
        else:
            mid = n//2
        
        
        stack.pop(mid)
        
        
        
        