class Queue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    
    def push(self, data):
        if not self.st1:
            self.st1.append(data)
            return
        
        while self.st1:
            self.st2.append(self.st1.pop())
        
        self.st2.append(data)
        while self.st2:
            self.st1.append(self.st2.pop())
        
    
    def pop(self):
        if not self.st1:
            return -1
        data = self.st1.pop()
        return data
    

    def peek(self):
        if not self.st1:
            return -1
        return self.st1[-1]
    
    def isEmpty(self):
        return len(self.st1) == 0



q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)


while not q.isEmpty():
    print(q.peek(), end=" ")
    q.pop()


    


    




    
