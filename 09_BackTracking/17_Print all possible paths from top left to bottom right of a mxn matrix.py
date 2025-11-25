
from typing import List
class Solution:
    def findAllPossiblePaths(self, n : int, m : int, grid : List[List[int]]) -> List[List[int]]:
        # code here
        
        ans = []
        
        def helper(i,j,curr):
            if i == n-1 and j == m-1:
                curr.append(grid[i][j])
                ans.append(curr[:])
                curr.pop()
                return
            
            curr.append(grid[i][j])
            
            if self.isSafe(i+1,j,grid):
                helper(i+1,j, curr)
                
            if self.isSafe(i,j+1,grid):
                helper(i,j+1, curr)
            
            
            curr.pop()
        
        helper(0,0,[])
        
        return ans
    
    
    def isSafe(self,i,j,grid):
        n = len(grid)
        m = len(grid[0])
        
        if i < 0 or j < 0 or i >=n or j >= m:
            return False
            
        return True
                
                
        
        
if __name__ == "__main__":
    sol = Solution()

    mat = [[1,2,3],[4,5,6]]
    n = len(mat)
    m = len(mat[0])

    print(sol.findAllPossiblePaths(n,m,mat))        
        
    # Output: 
    # [[1, 4, 5, 6], [1, 2, 5, 6], [1, 2, 3, 6]]
