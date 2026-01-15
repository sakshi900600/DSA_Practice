from collections import deque


class myStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        # push element on top
        self.q.appendleft(x)
        
        
    def pop(self):
        # remove top element
        if len(self.q) == 0:
            return 
    
        self.q.popleft()
        
    def top(self):
        # return top element
        if len(self.q) == 0:
            return -1
            
        return self.q[0]
        
    def size(self):
        # return current size
        return len(self.q)
        



if __name__ == "__main__":
    stack = myStack()
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.top())      # 6
    print(stack.size())     # 3
    stack.pop()
    print(stack.top())      # 5
    print(stack.size())     # 2




# pq  = deque()
# pq.append(4)
# pq.appendleft(5)
# pq.appendleft(6)
# # pq.popleft()
# # pq.pop()

# print(pq)
# print(pq[0])
# print(len(pq))