
class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = [0] * n

        # Initialize all spaces as free
        self.freeIndex = 0
        for i in range(n - 1):
            self.next[i] = i + 1

        # -1 is used to indicate end of free list
        self.next[n - 1] = -1

    # Function to check if queue 'qn' is empty
    def isEmpty(self, qn):
        return self.front[qn] == -1

    # Function to check if array is full
    def isFull(self):
        return self.freeIndex == -1

    # Function to enqueue 'x' into queue 'qn'
    def enqueue(self, x, qn):
        # Check if array is full
        if self.isFull():
            return False

        # Get next free index
        i = self.freeIndex
        self.freeIndex = self.next[i]

        # If queue is empty, update 
        # both front and rear
        if self.isEmpty(qn):
            self.front[qn] = i
        else:
            # Link new element to the previous rear
            self.next[self.rear[qn]] = i

        # Update rear
        self.rear[qn] = i

        # Store the element
        self.arr[i] = x

        # Mark end of queue
        self.next[i] = -1

        return True

    # Function to dequeue from queue 'qn'
    def dequeue(self, qn):
        # Check if queue is empty
        if self.isEmpty(qn):
            return -1

        # Get the front index of queue
        i = self.front[qn]

        # Update front
        self.front[qn] = self.next[i]

        # If queue becomes empty
        if self.front[qn] == -1:
            self.rear[qn] = -1

        # Add the dequeued position to free list
        self.next[i] = self.freeIndex
        self.freeIndex = i

        # Return the dequeued element
        return self.arr[i]


if __name__ == "__main__":
    n = 10
    k = 3
    queues = kQueues(n, k)

    print(queues.enqueue(10, 0), end=" ")
    print(queues.enqueue(20, 1), end=" ")
    print(queues.enqueue(30, 0), end=" ")
    print(queues.enqueue(40, 2), end=" ")

    print(queues.dequeue(0), end=" ")
    print(queues.dequeue(1), end=" ")
    print(queues.dequeue(2), end=" ")
    print(queues.dequeue(0), end=" ")
    print(queues.dequeue(0), end=" ")

    # Output:
    # True True True True 10 20 40 30 -1 