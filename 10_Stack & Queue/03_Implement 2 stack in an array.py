class TwoStacks:
    # based on constraint on gfg
    # def __init__(self):
    #     self.cap = 100
    #     self.top1 = -1
    #     self.top2 = 100
    #     self.cont = [0]*100

    # to check on local
    def __init__(self, cap):
        self.cap = cap
        self.top1 = -1
        self.top2 = cap
        self.cont = [0]*cap

    # Function to push an integer into stack 1
    def push1(self, x):
        # code here
        if self.top2-self.top1 <= 1:
            return -1
        
        self.top1 += 1
        self.cont[self.top1] = x
        return x
        
        

    # Function to push an integer into stack 2
    def push2(self, x):
        # code here
        if self.top2-self.top1 <= 1:
            return -1
        
        self.top2 -= 1
        self.cont[self.top2] = x
        return x

    # Function to remove an element from top of stack 1
    def pop1(self):
        # code here
        if self.top1 == -1:
            return -1
        
        data = self.cont[self.top1]
        self.top1 -= 1
        return data

    # Function to remove an element from top of stack 2
    def pop2(self):
        # code here
        if self.top2 >= self.cap:
            return -1
        
        data = self.cont[self.top2]
        self.top2 += 1
        return data
        
            
        
        
        
if __name__ == "__main__":
    ts = TwoStacks(4)

    # push into stack 1
    print(ts.push1(2), end=" ")
    print(ts.push1(4), end=" ")

    # push into stack 2
    print(ts.push2(3), end=" ")
    print(ts.push2(5), end=" ")
    print(ts.push1(15), end=" ")

    print("\n")

    # pop from stack 1 and stack 2
    print(ts.pop1(), end=" ")
    print(ts.pop2(), end=" ")