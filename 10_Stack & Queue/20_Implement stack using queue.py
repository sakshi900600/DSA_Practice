from collections import deque

class Stack_2queue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    

    def push(self, data):
        if not self.q1:
            self.q1.append(data)
        else:
            while len(self.q1) > 0:
                self.q2.append(self.q1.popleft())
            self.q1.append(data)

            while len(self.q2) > 0:
                self.q1.append(self.q2.popleft())

    
    def pop(self):
        if not self.q1:
            return -1
        return self.q1.popleft()


    def peek(self):
        if not self.q1:
            return -1
        return self.q1[0]


    def isEmpty(self):
        return len(self.q1) == 0


class Stack_1queue:
    def __init__(self):
        self.q = deque()
    

    def push(self, data):
        self.q.append(data)
        self.rotate()
        

    def pop(self):
        if not self.q:
            return -1
        return self.q.popleft()

    
    def peek(self):
        if not self.q:
            return -1
        return self.q[0]
    

    def isEmpty(self):
        return len(self.q) == 0


    # rotate by 1
    def rotate(self):
        # pop from front and push from back, from q till n-1 and its rotated.
        n = len(self.q)

        for i in range(n-1):
            front = self.q.popleft()
            self.q.append(front)
   


def st_2q():

    st = Stack_2queue()
    st.push(4)
    st.push(5)
    st.push(6)

    while not st.isEmpty():
        print(st.peek(), end=" ")
        st.pop()

    # Output: 6,5,4


def st_1q():

    st = Stack_1queue()
    st.push(4)
    st.push(5)
    st.push(6)

    while not st.isEmpty():
        print(st.peek(), end=" ")
        st.pop()

    # Output: 6,5,4




# st_2q()
st_1q()



