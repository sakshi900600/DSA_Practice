import heapq

class Solution:
    def findSmallestRange(self, mat):
        # code here
        n = len(mat)
        k = len(mat[0])
        
        min_heap = []
        max_val = float('-inf')
        
        for i in range(n):
            max_val = max(max_val, mat[i][0])
            # put (val, row, col)
            heapq.heappush(min_heap, (mat[i][0], i,0))
        
        
        min_range = float('inf')
        min_elem = float('inf')
        max_elem = float('-inf')
        
        while True:
            min_val, row, col = heapq.heappop(min_heap)
            
            curr_range = max_val - min_val
            
            if curr_range < min_range:
                min_range = curr_range
                min_elem = min_val
                max_elem = max_val
            
            if col+1 >= k:
                break
            
            next_val = mat[row][col+1]
            max_val = max(max_val, next_val)
            heapq.heappush(min_heap, (next_val, row,col+1))
            
        
        return [min_elem, max_elem]
            
                
                
                
                
if __name__ == "__main__":
    sol = Solution()
    
    mat = [[4, 7,9,12,15],
           [0, 8, 10, 14,20],
           [6, 12, 16, 30, 50]]
    
    print(sol.findSmallestRange(mat))        
    # Output: [6, 8]
        