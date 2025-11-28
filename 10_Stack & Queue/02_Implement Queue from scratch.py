
# 1. Implement simple queue using array, no space reuse.

class simple_q():
    def __init__(self, cap):
        self.cap = cap
        self.front = -1
        self.rear = -1
        self.container = [0]*cap
    

    def push(self, data):
        # overflow
        if self.rear >= self.cap-1:
            return None
        
        if self.front == self.rear == -1:
            self.front = 0
            self.rear = 0

            self.container[self.rear] = data
        
        else:
            self.rear += 1
            self.container[self.rear] = data
    

    def pop(self):
        if self.front == -1 or self.front > self.rear:
            return None

        if self.front > self.rear:
            self.front = -1
            self.rear = -1
        
        data = self.container[self.front]
        self.front += 1
        return data
    

    def peek(self):
        if self.front == -1 or self.front > self.rear:
            return None
        
        return self.container[self.front]
    

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    

    def size(self):
        if self.isEmpty():
            return 0

        return self.rear - self.front + 1


def Q1():

    q = simple_q(5)
    q.push(1)
    q.push(2)
    q.push(3)
    # q.push(4)
    # q.push(5)
    # print(q.push(6))

    # q.pop()
    # q.pop()
    # q.pop()
    # print(q.pop())
    # print(q.peek())
    # print(q.isEmpty())
    print(q.size())


    while not q.isEmpty():
        print(q.peek(), end=" ")
        q.pop()



# Dynamic or circular queue implementation using array.

class circular_q():
    def __init__(self, cap):
        self.cap = cap
        self.front = -1
        self.rear = -1
        self.container = [0]*cap
    

    def push(self, data):
        if self.isFull():
            return None
        
        if self.front == self.rear == -1:
            self.front = 0
            self.rear = 0

            self.container[self.rear] =  data
        
        else:
            self.rear = (self.rear+1) % self.cap
            self.container[self.rear] = data

    

    def pop(self):
        if self.isEmpty():
            return None
        
        if self.size() == 1:
            data = self.container[self.front]
            self.front = -1
            self.rear = -1
            return data
   
        data = self.container[self.front]
        self.front = (self.front + 1) % self.cap
        return data
    

    def peek(self):
        if self.isEmpty():
            return None
        
        return self.container[self.front]
    

    def isEmpty(self):
        return self.front == -1
    
    def isFull(self):
        return (self.front != -1) and (self.rear+1)% self.cap == self.front


    def size(self):
        if self.isEmpty():
            return 0
        
        if self.front <= self.rear:
            return (self.rear - self.front)+1
        else:
            return (self.cap-self.front) + (self.rear+1)
    



def Q2():
    q = circular_q(5)
    print(q.isEmpty())
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    print(q.push(6))

    # q.pop()
    # q.pop()
    # q.pop()
    # q.pop()
    # q.pop()
    # print(q.pop())
    print(q.peek())
    # print(q.isEmpty())
    # print(q.isFull())
    print(q.size())


    while not q.isEmpty():
        print(q.peek(), end=" ")
        q.pop()







# Q1()
Q2()