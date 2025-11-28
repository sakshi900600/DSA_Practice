# 1. Implementation of stack using array
# 1. Implementation of stack using linked list


# 1.
class Stack():
    def __init__(self, cap):
        self.cap = cap
        self.top = -1
        self.container = [0]*cap

    
    def push(self, data):
        # Overflow
        if self.top >= self.cap-1:
            return None
        
        self.top += 1
        self.container[self.top] = data
    

    def pop(self):
        # Underflow
        if self.top == -1:
            return None
        
        data = self.container[self.top]
        self.container[self.top] = None # not necessary but ok.
        self.top -= 1
        return data
    

    def peek(self):
        if self.top == -1:
            return None
        
        return self.container[self.top]
    

    def isEmpty(self):
        return self.top == -1
    

    def size(self):
        return self.top + 1
    


st = Stack(5)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
print(st.push(6))


# print(st.pop())
# print(st.peek())
# print(st.isEmpty())
# print(st.size())

while not st.isEmpty():
    print(st.peek(), end=" ")
    st.pop()


