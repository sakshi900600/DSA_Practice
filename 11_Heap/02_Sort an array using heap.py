class Solution:
    def heapSort(self, arr):
        #code here
        n = len(arr)
        
        # build heap
        last_non_leaf = (n//2)-1
        
        for i in range(last_non_leaf, -1, -1):
            self.heapify(arr, n, i)
        
        
        # swap first and last
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
            
        
    # Don't get confused: Using max-heap then getting sorted value in ascending order:
    # See in the above fun we are taking the max value and pushing it to the end everything that's why ascending sorted. 

    def heapify(self, arr, n, i):
        largest = i
        left = (2*i) + 1
        right = (2*i) + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)
            
            

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    sol = Solution()
    sol.heapSort(arr)

    print(arr)
    # Output: [1,2,3,4,5]

