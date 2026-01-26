#User function Template for python3
import heapq
class Solution():
    def mergeHeaps(self, a, b, n, m):
        #your code here
        
        pq = []
        
        for elem in a:
            heapq.heappush(pq, -elem)
        
        for elem in b:
            heapq.heappush(pq, -elem)
        
        ans = []
        while pq:
            ans.append(-heapq.heappop(pq))
            
        
        return ans
            
            
        
        
if __name__ == "__main__":
    a = [10, 5, 6, 2]
    b = [12, 7, 9]
    n = len(a)
    m = len(b)
    sol = Solution()
    print(sol.mergeHeaps(a, b, n, m))  
    # Output: [12, 10, 9, 7, 6, 5, 2]