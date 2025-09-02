class Solution:
    def spirallyTraverse(self, mat):
       # code here
       
        row = len(mat)
        col = len(mat[0])
        
        
        top = 0
        right = col-1
        bottom = row-1
        left = 0
        
        spiral_elem = []
        
        while top <= bottom and left <= right:
        
            # print top row:
            for j in range(left,right+1):
                spiral_elem.append(mat[top][j])
            
            top += 1
        
            # print right col:
            for i in range(top,bottom+1):
                spiral_elem.append(mat[i][right])
            
            right -= 1
        
            # print bottom row:
            if top <= bottom:
                for j in range(right,left-1,-1):
                    spiral_elem.append(mat[bottom][j])
                
                bottom -= 1
            
            # print left col:
            if left <= right:
                for i in range(bottom,top-1,-1):
                    spiral_elem.append(mat[i][left])
                
                left += 1
        
        
        return spiral_elem


    # why checking before printing bottom row and left col??
    # -
    # coz when only one row lefts to print then the first loop prints that, for right nothing lefts but bottom and left was running and causing duplicates that's why checking using if before printing. (CHAMK GAYA 😄)




if __name__ == "__main__":
    sol = Solution()

    # input:
    mat = [[2,7,10],[5,1,3],[4,2,8]]
    # output: [2, 7, 10, 3, 8, 2, 4, 5, 1]

    # mat = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
    # output: 
    # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]


    print(sol.spirallyTraverse(mat))


        
