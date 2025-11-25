import heapq
class Solution:
   def minCost(self, arr):
    # code here
    
    pq = []
    
    for i in range(len(arr)):
        heapq.heappush(pq, arr[i])
    
    
    total_cost = 0
    while len(pq) > 1:
        e1 = heapq.heappop(pq)
        e2 = heapq.heappop(pq)
        
        curr_cost = e1 + e2
        total_cost += curr_cost
        heapq.heappush(pq, curr_cost)
    
    
    return total_cost
        



if __name__ == "__main__":
    arr = [4, 3, 2, 6]
    sol = Solution()
    print(sol.minCost(arr))  # Output: 29