
class Solution:
    def solveSudoku(self, mat):
        # code here
        
        
        def helper(i,j):
            if i == 8 and j == 9:
                return True
                
            if j == 9:
                i += 1
                j = 0
            
            if mat[i][j] != 0:
                return helper(i,j+1)
            
            for num in range(1, 10):
                if self.isSafe(i,j,num, mat):
                    mat[i][j] = num
                    if helper(i,j+1):
                        return True
                    mat[i][j] = 0  
            
            return False
        
        return helper(0,0)
        
         
        
        
    def isSafe(self, r,c, opt, mat):
        # row
        for j in range(9):
            if mat[r][j] == opt:
                return False
            
        # col
        for i in range(9):
            if mat[i][c] == opt:
                return False
            
        # 3x3 grid
        start_r = r - (r % 3)
        start_c = c - (c % 3)
            
        for i in range(3):
            for j in range(3):
                if mat[start_r+i][start_c+j] == opt:
                    return False
            
        return True
            
            
            
            

if __name__ == "__main__":

    mat = [
        [3,0,6,5,7,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,8,6,3,0,0]
    ]

    sol = Solution()
    print(sol.solveSudoku(mat)) #True

    print(mat)

    # Output:
    # [[3, 1, 6, 5, 7, 8, 4, 9, 2],
    # [5, 2, 9, 1, 3, 4, 7, 6, 8],
    # [4, 8, 7, 6, 2, 9, 5, 3, 1],
    # [2, 6, 3, 4, 1, 5, 9, 8, 7], 
    # [9, 7, 4, 8, 6, 3, 1, 2, 5], 
    # [8, 5, 1, 7, 9, 2, 6, 4, 3], 
    # [1, 3, 8, 9, 4, 7, 2, 5, 6], 
    # [6, 9, 2, 3, 5, 1, 8, 7, 4], 
    # [7, 4, 5, 2, 8, 6, 3, 1, 9]]