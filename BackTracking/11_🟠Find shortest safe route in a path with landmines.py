from typing import List

# Works fine but TLE
class Solution:
    def findShortestPath(self, mat : List[List[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])

        # mark all 0 cells adjacent cell as 0
        new_mat = [row[:] for row in mat]
        nr = [-1,0,1,0]
        nc = [0,1,0,-1]


        for i in range(n):
            for j in range(m):
                if new_mat[i][j] == 0:
                    for x in range(4):
                        adjr = i + nr[x]
                        adjc = j + nc[x]

                        if (0<= adjr <n) and (0<= adjc <m):
                            mat[adjr][adjc] = 0


        visited = [[False]*m for _ in range(n)]
        shortest = [float('inf')]

        # call helper fun from 1 col non-zero cell
        for r in range(n):
            if mat[r][0] != 0:
                self.helper(r,0,mat,0,shortest,visited)
        

        if shortest[0] != float('inf'):
            return shortest[0]
        
        return -1



    
    def helper(self, row, col, mat, count, shortest, visited):
        n = len(mat)
        m = len(mat[0])

        if col == m-1:
            count += 1
            shortest[0] = min(shortest[0], count)
            count -= 1
            return
        
        nr = [-1,0,1,0]
        nc = [0,1,0,-1]

        
        # explore all 4 moves
        for x in range(4):
            adjr = row + nr[x]
            adjc  = col + nc[x]

            if (0<= adjr <n) and (0<= adjc <m) and visited[adjr][adjc] == False and mat[adjr][adjc] != 0:
                visited[row][col] = True
                self.helper(adjr, adjc, mat, count+1, shortest, visited)
                visited[row][col] = False
        
        
        

        
  
        



if __name__ == "__main__":

    mat = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
    ]
    # Output: 6

    mat = [ [1, 1, 1, 1, 1],
      [1, 1, 0, 1, 1],
      [1, 1, 1, 1, 1] ]
    # Output -1

    sol = Solution()
    ans = sol.findShortestPath(mat)
    print(ans)