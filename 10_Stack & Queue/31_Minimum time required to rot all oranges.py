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
        
        
        
                    
    
    
    