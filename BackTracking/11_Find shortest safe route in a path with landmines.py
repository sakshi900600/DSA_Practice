from typing import List

class Solution:
    def findShortestPath(self, mat : List[List[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        
        # mark 0th adjacent cells as -1
        # final_mat = mat.copy()
        final_mat = [row[:] for row in mat]
        
        # all 4 directions moves val
        rn = [-1,0,1,0]
        cn = [0,1,0,-1]
        
        for i in range(n):
            for j in range(m):
                if final_mat[i][j] == 0:
                    # all 4 moves
                    for x in range(4):
                        adjr = i + rn[x]
                        adjc = j + cn[x]
                        
                        if adjr>=0 and adjc>=0 and adjr<n and adjc<m:
                            final_mat[adjr][adjc] = -1
        
        
        # now change all marked val as 0
        for i in range(n):
            for j in range(m):
                if final_mat[i][j] == -1:
                    final_mat[i][j] = 0
        
        
        
        
        
        
        
        def helper(row, col, count, short_path):
            if col == m-1:
                short_path[0] = min(short_path[0], count)
                return
            
            
            for x in range(4):
                adjr = row + rn[x]
                adjc = col + cn[x]
                
                if self.isSafe(adjr, adjc, final_mat):
                    count += 1
                    final_mat[adjr][adjc] = 2
                    
                    helper(adjr, adjc, count, short_path)
                    final_mat[adjr][adjc] = 1
                    count -= 1
                    
           
        
        short_path = [float('inf')] 
        # start finding path from any row of 1st col with non-zero val
        for i in range(n):
            if final_mat[i][0] != 0:
                helper(i,0,1,short_path)
        
        
        if short_path[0] != float('inf'):
            return short_path[0]
        else:
            return -1
        
        
        
    
    def isSafe(self, row, col, mat):
        n = len(mat)
        m = len(mat[0])
        
        if row<0 or col<0 or row>=n or col>=m or mat[row][col] == 0 or mat[row][col] == 2:
            return False
        
        return True
        
        
        

        
  
        

if __name__ == "__main__":

    mat = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
    ]
    
    sol = Solution()
    ans = sol.findShortestPath(mat)
    print(ans)