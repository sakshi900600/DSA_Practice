from collections import deque

class Solution:

    # tle ------------------
    def orangesRot(self, mat):
        # code here
        
        row = len(mat)
        col = len(mat[0])
        
        nrow = [-1,0,1,0]
        ncol = [0,1,0,-1]
        
        
        def ispart(i,j):
            c1 = 0 <= i < row
            c2 = 0 <= j < col
            
            return c1 and c2
        
        
        time = 0
        change = False
        
        while True:
            for i in range(row):
                for j in range(col):
                    if mat[i][j] == time + 2:
                        
                        for x in range(4):
                            new_r = i + nrow[x]
                            new_c = j + ncol[x]
                            
                            if ispart(new_r, new_c) and mat[new_r][new_c] == 1:
                                mat[new_r][new_c] += mat[i][j]
                                change = True
            
            if change == False:
                break
            
            change = False
            time += 1
        
        
        # checking if any lefts
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    return -1
        
        
        return time
        

    # optimal bfs ------------------     
    def orangesRot2(self, mat):
        # code here
        
        row = len(mat)
        col = len(mat[0])
        
        nr = [-1,0,1,0]
        nc = [0,1,0,-1]
        
        def isValid(r,c):
            c1 = 0 <= r < row
            c2 = 0 <= c < col
            
            return c1 and c2
            
        
        q = deque()
        
        # put all 2 in queue
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 2:
                    q.append((i,j))
         
        time = 0
        
        while q:
            size = len(q)
            ischanged = False
            
            for _ in range(size):
                r,c = q.popleft()
                
                for x in range(4):
                    adjr = r + nr[x]
                    adjc = c + nc[x]
                    
                    if isValid(adjr,adjc) and mat[adjr][adjc] == 1:
                        mat[adjr][adjc] = 2
                        q.append((adjr,adjc))
                        ischanged = True
                        
            if ischanged:
                time += 1
          
          
        # checking if any lefts
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    return -1
        
        
        return time



if __name__ == "__main__":
    mat = [[2,1,0,2,1],
           [1,0,1,2,1],
           [1,0,0,2,1]]
    
    obj = Solution()
    print(obj.orangesRot(mat))

    # Output: 2


