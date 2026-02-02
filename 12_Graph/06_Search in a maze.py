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
        
        
    # def isSafe(self,i,j,maze):
    #     n = len(maze)
    #     return (
    #         (0 <= i < n) and (0 <= j <n) and maze[i][j] == 1
    #         )
        

    # using DFS :

    def ratInMaze_dfs(self, maze):
        # code here
        
        n = len(maze)
        m = len(maze[0])
        
        ans = []
        self.dfs(0,0,maze,"",ans)
        return ans
                  
    
    def dfs(self, i,j, maze,curr_path, ans):
        n = len(maze)
        m = len(maze[0])
        
        if i==n-1 and j==m-1:
            ans.append(curr_path)
            return
        
        maze[i][j] = 2
        
        adj = [(1,0,"D"), (0, -1,"L"), (0,1,"R"), (-1,0,"U")]
        
        for x in range(4):
            nr = i + adj[x][0]
            nc = j + adj[x][1]
            s = adj[x][2]
            
                
            if self.isSafe(nr,nc,maze):
                self.dfs(nr,nc,maze,curr_path+s, ans)
        
        maze[i][j] = 1
        
            
    def isSafe(self,i,j,maze):
        n = len(maze)
        return (
            (0 <= i < n) and (0 <= j <n) and maze[i][j] == 1
            )
    


if __name__ == "__main__":
    sol = Solution()

    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    # print(sol.ratInMaze(maze))
    print(sol.ratInMaze_dfs(maze))

    # Output: ['DDRDRR', 'DRDDRR']

    


    
    


        