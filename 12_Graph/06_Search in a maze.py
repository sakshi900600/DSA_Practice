class Solution:
    # using backtracking -:
    def ratInMaze(self, maze):
        # code here
        
        n = len(maze)
        ans = []
        
        def solve(i,j, path):
            if i == n-1 and j == n-1:
                ans.append(path)
                return
            
            maze[i][j] = 2
            # down
            if self.isSafe(i+1,j,maze):
                solve(i+1, j, path+'D')
            # left
            if self.isSafe(i,j-1,maze):
                solve(i, j-1, path+'L')
            # right
            if self.isSafe(i,j+1,maze):
                solve(i, j+1, path+'R')
            # up
            if self.isSafe(i-1,j,maze):
                solve(i-1, j, path+'U')
            
            maze[i][j] = 1
            
            
        solve(0,0,"")
        return ans
        
        
    def isSafe(self,i,j,maze):
        n = len(maze)
        return (
            (0 <= i < n) and (0 <= j <n) and maze[i][j] == 1
            )
        


    
    


        