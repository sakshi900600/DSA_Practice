import heapq
class Solution:
    def mergeArrays(self, mat):
        # Code here
        # 1. using list & sorting
        # 2. using heap / pq
        
        li = []
        pq = []
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                # li.append(mat[i][j])
                heapq.heappush(pq, mat[i][j])
        
        
        while pq:
            li.append(heapq.heappop(pq))
        
        
        return li



if __name__ == "__main__":
    mat = [[1, 3, 5],
           [2, 4, 6],
           [0, 9, 10]]
    sol = Solution()
    print(sol.mergeArrays(mat))  
    # Output: [0, 1, 2, 3, 4, 5, 6, 9, 10]



    