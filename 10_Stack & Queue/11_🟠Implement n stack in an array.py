class kStacks:

    def __init__(self, n, k):
        # initialize data structures for k stacks
        self.arr = [0] * n
        self.top = [-1] * k
        self.next = [0] * n
        self.freeTop = 0

        for i in range(n - 1):
            self.next[i] = i + 1
        self.next[n - 1] = -1
        

    def push(self, x, i):
        # push element x into stack i
        if self.freeTop == -1:
            # print("Stack Overflow")
            return

        index = self.freeTop
        self.freeTop = self.next[index]
        self.arr[index] = x
        self.next[index] = self.top[i]
        self.top[i] = index
        

    def pop(self, i):
        # pop element from stack i
        if self.top[i] == -1:
            # print("Stack Underflow")
            return -1

        index = self.top[i]
        self.top[i] = self.next[index]
        self.next[index] = self.freeTop
        self.freeTop = index

        return self.arr[index]
        
        
        
if __name__ == "__main__":
    k = 3
    n = 10
    ks = kStacks(n, k)

    ks.push(15, 2)
    ks.push(45, 2)

    ks.push(17, 1)
    ks.push(49, 1)
    ks.push(39, 1)

    ks.push(11, 0)
    ks.push(9, 0)
    ks.push(7, 0)

    print("Popped element from stack 2 is " + str(ks.pop(2)))
    print("Popped element from stack 1 is " + str(ks.pop(1)))
    print("Popped element from stack 0 is " + str(ks.pop(0)))


    # Output:
    # Popped element from stack 2 is 45
    # Popped element from stack 1 is 39
    # Popped element from stack 0 is 7

    