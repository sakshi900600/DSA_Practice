class Solution:
    def rowWithMax1s(self, arr):
        # code here
        
        n = len(arr)
        m = len(arr[0])
    
        max_one = 0
        row = -1
    
        for i in range(n):
            count_one = 0
            for j in range(m):
                count_one += arr[i][j]
    
                if count_one > max_one:
                    max_one = count_one
                    row = i
                    
        
        return row
    


if __name__ == "__main__":
    sol = Solution()


    # input:
    mat = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
    mat = [[0,0], [0,0]]

    # output:
    # 2
    # -1

    print(sol.rowWithMax1s(mat))