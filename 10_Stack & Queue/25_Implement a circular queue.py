class CircularQueue:
    def __init__(self, cap):
        self.cap = cap
        self.front = -1
        self.rear = -1
        self.size = 0
        self.cont = [0]*self.cap
    

    def push(self, data):
        if self.size == self.cap:
            return
        
        if self.front == self.rear == -1:
            self.front = 0
            self.rear = 0
            self.size += 1
            self.cont[self.rear] = data
            return
        
        self.rear = (self.rear+1) % self.cap
        self.cont[self.rear] = data
        self.size += 1

    
    def pop(self):
        if self.size == 0:
            return -1
        
        if self.front == self.rear:
            data = self.cont[self.front % self.cap]
            self.size = 0
            self.front = -1
            self.rear = -1
            return data

        data = self.cont[self.front % self.cap]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return data

    def peek(self):
        if self.size == 0:
            return
        
        return self.cont[self.front]
    
    def isFull(self):
        return self.size == self.cap

    def isEmpty(self):
        return self.size == 0


if __name__ == "__main__":

    # input:
    cq = CircularQueue(5)

    cq.push(1)
    cq.push(2)
    cq.push(3)
    cq.push(4)
    cq.push(5)
    cq.pop()
    cq.pop()
    cq.pop()
    cq.push(6)
    cq.push(7)

    while not cq.isEmpty():
        print(cq.peek(), end=" ")
        cq.pop()
    

    # 4 5 6 7




