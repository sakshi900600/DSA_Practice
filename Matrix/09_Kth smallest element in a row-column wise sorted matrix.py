class Solution:

    
    def kthSmallest(self, mat, k):
        # code here
        
        n = len(mat)
        m = len(mat[0])
        
        li = []
        
        for i in range(n):
            for j in range(m):
                li.append(mat[i][j])
                
        
        li.sort()
        return li[k-1]
        
    

if __name__ == "__main__":
    sol = Solution()

    # input:
    mat = [[16, 28, 60, 64],
            [22, 41, 63, 91],
            [27, 50, 87, 93],
            [36, 78, 87, 94]]

    k = 3

    # output: 27

    print(sol.kthSmallest(mat,k))
    

    