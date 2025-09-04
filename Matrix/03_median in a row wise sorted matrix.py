class Solution:
    def median(self, mat):
        # code here 
        
        n = len(mat)
        m = len(mat[0])
        li = []
        
        for i in range(n):
            for j in range(m):
                li.append(mat[i][j])
                
        li.sort()
        
        if len(li) % 2 != 0:
            return li[len(li) // 2]
        else:
            e1 = li[len(li) // 2]
            e2 = li[len(li) // 2 - 1]
            return (e1 + e2) / 2



if __name__ == "__main__":
    sol = Solution()

    # input:
    mat = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
    # Output: 5

    print(sol.median(mat))