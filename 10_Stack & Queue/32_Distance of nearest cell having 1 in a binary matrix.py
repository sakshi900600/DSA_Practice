from collections import deque

class Solution:
    # MY solution  - tle
    def nearest(self, grid):
        # code here
        
        n = len(grid)
        m = len(grid[0])

        vis = [[0]*m for _ in range(n)]
        
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    vis[i][j] = 1
                    q.append((i, j, 0))
        
        
        nr = [-1, 0, 1, 0]
        nc = [0, 1, 0, -1]
        
        
        def isvalid(r, c):
            c1 = 0 <= r < n
            c2 = 0 <= c < m
            
            return c1 and c2
            
        
        while q:
            r, c, d = q.popleft()
            grid[r][c] = d
            
            for x in range(4):
                adjr = r + nr[x]
                adjc = c + nc[x]
                
                if isvalid(adjr, adjc) and vis[adjr][adjc] == 0:
                    vis[adjr][adjc] = 1  
                    q.append((adjr, adjc, d + 1))
        
        
        return grid
        
        
    def nearest2(self, grid):
        # code here
        
        n = len(grid)
        m = len(grid[0])

        ans = [[float('inf')]*m for _ in range(n)]
        
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans[i][j] = 0
                    q.append((i, j))
        
        
        nr = [-1, 0, 1, 0]
        nc = [0, 1, 0, -1]
        
        
        def isvalid(r, c):
            c1 = 0 <= r < n
            c2 = 0 <= c < m
            
            return c1 and c2
            
        
        while q:
            size = len(q)
            
            for _ in range(size):
                r,c = q.popleft()
            
                for x in range(4):
                    adjr = r + nr[x]
                    adjc = c + nc[x]
                    
                    if isvalid(adjr, adjc) and ans[adjr][adjc] == float('inf'):
                        ans[adjr][adjc] = ans[r][c] + 1  
                        q.append((adjr, adjc))
        
        
        return ans




if __name__ == "__main__":
    grid = [[0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]]
    solution = Solution()
    # result = solution.nearest(grid)
    result = solution.nearest2(grid)
    print(result)

    # Output:
    # [[2, 1, 2],
    #  [1, 0, 1],
    #  [0, 0, 0]]




