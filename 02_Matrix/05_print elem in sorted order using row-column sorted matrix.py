import heapq
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
    

    # coz all rows are sorted so the problem comes down to merge k sorted arrays.
    # so we will use min-heap and start with the first elem of each row and keep on popping the min and adding in ans and then if the popped elems col+1 is less than m then put them into heap and the end elem will be stored in sorted order in ans list.

    # here we will add val along with row,col in heap so that we can move the pointer (col) and keep of traversing on each elem

    def sorted_mat(self, mat):
        n = len(mat)
        m = len(mat[0])

        pq = []

        for i in range(n):
            heapq.heappush(pq, (mat[i][0], i ,0))
        
        ans = []

        while pq:
            val,row,col = heapq.heappop(pq)
            ans.append(val)

            if col+1 < m:
                heapq.heappush(pq, (mat[row][col+1], row ,col+1))

        return ans



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
    print(sol.sorted_mat(mat))
    