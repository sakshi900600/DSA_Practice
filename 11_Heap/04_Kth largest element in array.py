import heapq

class Solution:
    def kLargest(self, arr, k):
        # Your code here
        n = len(arr)
        
        pq = []
        
        for i in range(n):
            heapq.heappush(pq, -arr[i])
        
        ans = []
        for i in range(k):
            ans.append(-heapq.heappop(pq))
        
        return ans
        



if __name__ == "__main__":
    arr = [3,2,1,5,6,4]
    k = 2
    sol = Solution()
    print(sol.kLargest(arr, k))  
    # Output: [6, 5]