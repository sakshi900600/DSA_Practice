class Solution:
    def snakePattern(self, mat): 
        # code here 
        
        ans = []
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            if i % 2 == 0:
                for j in range(m):
                    ans.append(mat[i][j])
            else:
                for j in range(m-1, -1, -1):
                    ans.append(mat[i][j])
        
        return ans
    

    # shorter code:
    def snakePattern(self, mat): 
        # code here 
        
        ans = []
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            if i % 2 == 0:
                ans.extend(mat[i])
            else:
                
                ans.extend(reversed(mat[i]))
        
        return ans
    
    

