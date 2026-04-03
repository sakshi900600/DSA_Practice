#User function Template for python3

class Solution:
    def searchWord(self, grid, word):
        n = len(grid)
        m = len(grid[0])
        result = []
        
        # Check each cell as potential starting point
        for i in range(n):
            for j in range(m):
                if grid[i][j] == word[0]:
                    # Check all 8 directions from this starting cell
                    if self.hasWordInAnyDirection(i, j, grid, word):
                        result.append([i, j])
        
        return result
        
        
    
    def hasWordInAnyDirection(self, r, c, grid, word):

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        # Try each direction
        for dr, dc in directions:
            if self.checkDirection(r, c, dr, dc, grid, word):
                return True
                
                
        return False
        
    
    def checkDirection(self, r, c, dr, dc, grid, word):
        n = len(grid)
        m = len(grid[0])
        
        # Check if word fits in this direction
        for i in range(len(word)):
            nr = r + (dr * i)
            nc = c + (dc * i)
            
            # Check bounds
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                return False
            
            # Check character match
            if grid[nr][nc] != word[i]:
                return False
        
        return True
        
        


