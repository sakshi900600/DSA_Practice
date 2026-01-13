class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        
        knows = [0]*n
        knownBy = [0]*n
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                if mat[i][j] == 1:
                    knows[i] += 1
                    knownBy[j] += 1
        
        
        for i in range(n):
            if knows[i] == 0 and knownBy[i] == n-1:
                return i
        
        
        return -1
        


if __name__ == "__main__":
    mat = [[0, 1, 0],
           [0, 0, 0],
           [0, 1, 0]]
    sol = Solution()
    print(sol.celebrity(mat))