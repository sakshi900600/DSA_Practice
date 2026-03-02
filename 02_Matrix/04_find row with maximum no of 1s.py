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
    

    def rowWithMax1s_bs(self, arr):
        # code here
        m = len(arr[0])
        max_count = 0
        row = -1
        
        for i in range(len(arr)):
            lb = self.lowerBound(arr[i], 1)
            
            if lb != m:
                ones = m - lb
                if ones > max_count:
                    max_count = ones
                    row = i
        
        return row        
        
        
        
    def lowerBound(self, arr, tar):
        n = len(arr)
        si = 0
        ei = n-1
        
        ans = n
        
        while si <= ei:
            mid = (si+ei)//2
            
            if arr[mid] >= tar:
                ans = mid
                ei = mid-1
            else:
                si = mid+1
        
        
        return ans



if __name__ == "__main__":
    sol = Solution()


    # input:
    mat = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
    # mat = [[0,0], [0,0]]

    # output:
    # 2
    # -1

    print(sol.rowWithMax1s(mat))
    print(sol.rowWithMax1s_bs(mat))