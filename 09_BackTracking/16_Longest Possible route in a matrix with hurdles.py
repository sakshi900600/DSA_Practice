

class Solution:
    def longestPath(self,mat : list[list[int]],n : int, m : int, xs : int, ys : int, xd : int, yd : int) -> int:
        # code here
        
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1
        
        
    
        def helper(row, col, count, longest):
            if row == xd and col == yd:
                longest[0] = max(longest[0], count)
                return True
            
            nr = [-1,0,1,0]
            nc = [0,1,0,-1]
            
            for x in range(4):
                adjr = row + nr[x]
                adjc = col + nc[x]
                
                if 0<=adjr<n and 0<=adjc<m and visited[adjr][adjc]==False and mat[adjr][adjc]!=0:
                    visited[row][col] = True
                    if (helper(adjr, adjc, count+1, longest)):
                        return True
                        
                    visited[row][col] = False
        
        
        visited = [[False]*m for _ in range(n)]
        longest = [float('-inf')]
        
        if(helper(xs,ys, 0, longest)):
            return longest[0]
        
        # if longest[0] != float('-inf'):
            # return longest[0]
        
        
        return -1
        
        


if __name__ == "__main__":

    # mat = [
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # ]
    # xs, ys = 0,0
    # xd, yd = 1,7
    # Output: 24


    mat = [
        [1,0,0,1,0],
        [0,0,0,1,0],
        [0,1,1,0,0]
    ]
    # xs, ys = 0,3
    # xd, yd = 1,3
    # Output: -1


    mat = [
        [1,0,1,0],
        [0,1,1,0],
        [1,1,1,1]
    ]
    xs, ys = 1,1
    xd, yd = 2,3
    # Output: 3

    n = len(mat)
    m = len(mat[0])
    

    sol = Solution()
    print(sol.longestPath(mat, n,m,xs,ys,xd,yd))
    
