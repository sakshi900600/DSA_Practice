#User function Template for python3

class Solution:
    def convertMinToMaxHeap(self, N, arr):
        # Code here
        last_non_leaf = (N//2)-1
        
        for i in range(last_non_leaf, -1, -1):
            self.heapify(arr, N, i)
    
    
    def heapify(self, arr, n, i):
        largest = i
        left = (2*i)+1
        right = (2*i)+2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right<n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr,n, largest)
            
            

if __name__ == "__main__":
    arr = [3,5,9,6,8,20,10,12,18,9]
    N = len(arr)
    
    sol = Solution()
    sol.convertMinToMaxHeap(N, arr)
    
    print("Max Heap array:")
    print(arr)

    # Output:
    # Max Heap array:
    # [20, 18, 10, 12, 9, 9, 3, 5, 6, 8]

    