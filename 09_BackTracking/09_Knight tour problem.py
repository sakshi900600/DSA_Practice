from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        # Code here
        sr = knightPos[0]
        sc = knightPos[1]
        tr = targetPos[0]
        tc = targetPos[1]
        
        return self.bfs(sr, sc, tr, tc, n)
    
    
    def bfs(self, sr, sc, tr, tc, n):
        visited = [[0] * (n + 1) for _ in range(n + 1)]
        q = deque()
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        visited[sr][sc] = 1
        q.append((sr, sc, 0))
        
        while q:
            node = q.popleft()
            row = node[0]
            col = node[1]
            dist = node[2]
            
            if row == tr and col == tc:
                return dist
            
            for i in range(8):
                nr = row + moves[i][0]
                nc = col + moves[i][1]
                
                if self.isSafe(nr, nc, n) and visited[nr][nc] == 0: 
                    visited[nr][nc] = 1
                    q.append((nr, nc, dist + 1))
        
        return -1
        
    
    def isSafe(self, r, c, n):
        c1 = 1 <= r <= n
        c2 = 1 <= c <= n
        return c1 and c2
        
        
        

if __name__ == "__main__":
    knightPos = [4, 5]
    targetPos = [1, 1]
    n = 6
    sol = Solution()
    print(sol.minStepToReachTarget(knightPos, targetPos, n))  
    # Output: 3

    