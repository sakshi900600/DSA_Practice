class Solution:

    # tle -------------
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        return self.helper(n,sum,arr)
        
    
    def helper(self, n, csum,arr):
        if n == 0:
            return False
        
        if csum == 0:
            return True
            
        
        if arr[n-1] > csum:
            return self.helper(n-1,csum,arr)
        
        # take
        take = self.helper(n-1, csum-arr[n-1],arr)
        nottake = self.helper(n-1, csum,arr)
        
        return take or nottake
        
        
if __name__ == "__main__":
    sol = Solution()

    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    print(sol.isSubsetSum(arr,sum))
    # Output: True
    
