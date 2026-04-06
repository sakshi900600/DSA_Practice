# Its House Robber problem 

class Solution:  
    def findMaxSum(self, arr):
        # code here
        n = len(arr)
        dp = [-1]*n
        return self.helper(arr,0,dp)
        
    
    def helper(self, arr, idx,dp):
        if idx >= len(arr):
            return 0
        
        if dp[idx] != -1:
            return dp[idx]
        
        take = arr[idx] + self.helper(arr,idx+2,dp)
        nottake = 0 + self.helper(arr,idx+1,dp)
        
        dp[idx] = max(take, nottake)
        return dp[idx]
        
        

if __name__ == "__main__":
    sol = Solution()

    arr = [6, 7, 1, 3, 8, 2, 4]
    print(sol.findMaxSum(arr))

    # Output: 19
    