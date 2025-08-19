class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        sum = arr[0]
        maxSum = arr[0]
        
        for i in range(1,len(arr)):
            if sum >= 0 :
                sum += arr[i]
            else:
                sum = arr[i]
            
            
            if sum > maxSum:
                maxSum = sum
            
        
        return maxSum
    



if __name__ == '__main__':

    sol = Solution()

    # input:
    arr = [2, 3, -8, 7, -1, 2, 3]
    # output: 11
    
    print(sol.maxSubarraySum(arr))