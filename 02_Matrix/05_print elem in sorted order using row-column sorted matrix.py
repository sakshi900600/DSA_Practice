
class Solution:
    def sortedMatrix(self,n,mat):
        #code here
        
        
        li = []
        for i in range(n):
            for j in range(n):
                li.append(mat[i][j])
        
        
        li.sort()
        # print(li)
        k = 0
        
        for i in range(n):
            for j in range(n):
                if k < n*n:
                    mat[i][j] = li[k]
                    k += 1
        
        return mat



if __name__ == "__main__":
    sol = Solution()

    # input:
    n=4
    mat=[[10,20,30,40],
    [15,25,35,45], 
    [27,29,37,48] ,
    [32,33,39,50]]


    # output:
    # [[10, 15, 20, 25], [27, 29, 30, 32], [33, 35, 37, 39], [40, 45, 48, 50]]

    print(sol.sortedMatrix(n,mat))