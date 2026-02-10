
# Logic: Simply find out not of connected components in graph. For that called dfs and dfs marks all adjacents cells. So as many times we call dfs, that many number of islands are there.


class Solution:
    def numIslands(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        
        vis = [[0]*m for _ in range(n)]
        island = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and vis[i][j]==0:
                    island += 1
                    self.dfs(i,j,vis,grid)
                    
        
        return island
        
    
    def dfs(self, row, col, vis,mat):
        vis[row][col] = 1
        
        next_moves = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        
        for i in range(8):
            nr = row + next_moves[i][0]
            nc = col + next_moves[i][1]
            
            if self.isSafe(nr, nc,mat) and mat[nr][nc] == 'L' and vis[nr][nc]==0:
                self.dfs(nr, nc, vis, mat)
                

    def isSafe(self,row, col, mat):
        n = len(mat)
        m = len(mat[0])
        c1 = 0 <= row < n
        c2 = 0 <= col < m
        
        return c1 and c2 
        
        
        
        
if __name__ == "__main__":
    grid = [['L', 'L', 'W', 'W', 'W'], 
                ['W', 'L', 'W', 'W', 'L'], 
                ['L', 'W', 'W', 'L', 'L'], 
                ['W', 'W', 'W', 'W', 'W'], 
                ['L', 'W', 'L', 'L', 'W']]
    
    solution = Solution()
    print(solution.numIslands(grid))  
    # Output: 4
     
           
        
    