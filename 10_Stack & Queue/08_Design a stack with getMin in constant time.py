class Stack:
    def __init__(self):
        self.cap = 10000
        self.cont = [0]*10000
        self.top = -1
        self.mini = -1
        self.min_st = [0]*10000
    

    def push(self, data):
        if self.top >= self.cap-1:
            return None
        self.top += 1
        self.cont[self.top] = data

        if self.mini == -1:
            self.mini += 1
            self.min_st[self.mini] = data
        else:
            if data < self.min_st[self.mini]:
                self.mini += 1
                self.min_st[self.mini] = data
    

    def pop(self):
        if self.top == -1:
            return None
        
        data = self.cont[self.top]
        self.top -= 1

        if data == self.min_st[self.mini]:
            self.mini -= 1
        
        return data
    
    def getMin(self):
        if self.mini == -1:
            return None
        
        return self.min_st[self.mini]
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top >= self.cap-1
    
def execution():
    st = Stack()

    print(st.isEmpty())
    print(st.isFull())

    st.push(5)
    st.push(2)
    st.push(3)

    print(st.pop())

    print(st.isEmpty())
    print(st.isFull())

    st.push(1)
    print(st.getMin())

    while not st.isEmpty():
        print(st.pop(), end=" ")


execution()
# Output:
'''
True
False
3
False
False
1
1 2 5
'''


# gfg code: ---------------------------------------------------------
# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    # Code here
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    # Code here
    data = arr[-1]
    arr.pop()
    return arr

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    return len(arr) == n

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    return len(arr) == 0

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    mini = float('inf')
    while not isEmpty(arr):
        mini = min(mini, arr[-1])
        arr.pop()
    
    return mini
    
    
    
