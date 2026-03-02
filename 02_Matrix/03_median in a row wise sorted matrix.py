class Solution:

    # Time Complexity: O(n*m*log(n*m)) 
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


    # optimized soln: 

    def median_opt(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # Find min and max elements
        minVal = float('inf')
        maxVal = float('-inf')
        
        for i in range(n):
            minVal = min(mat[i][0], minVal)
            maxVal = max(mat[i][m-1], maxVal)
        
        
        # Required position of median (1-based index)
        req = (n * m +1) // 2
        
        # Binary search for the median
        si = minVal
        ei = maxVal
        
        while si <= ei:
            mid = (si + ei) // 2
            
            # Count elements less than or equal to mid
            count = 0
            for i in range(n):
                count += self.upperBound(mat[i], mid)
            
            if count < req:
                si = mid + 1
            else:
                ei = mid - 1
        
        return si
    
    
    def upperBound(self, arr, tar):
        n = len(arr)
        
        ans = n  # Default to n if all elements are <= tar
        si = 0
        ei = n - 1
        
        while si <= ei:
            mid = (si + ei) // 2
            
            if arr[mid] > tar:
                ans = mid
                ei = mid - 1
            else:
                si = mid + 1
        
        return ans



if __name__ == "__main__":
    sol = Solution()

    # input:
    mat = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
    # Output: 5

    print(sol.median(mat))
    print(sol.median_opt(mat))

    