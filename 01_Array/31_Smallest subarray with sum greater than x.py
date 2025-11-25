class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        sum = 0
        minlen = float('inf')
        
        left = 0
        for right in range(len(arr)):
            sum += arr[right]
            
            while sum > x:
                minlen = min(minlen, right-left+1)
                sum -= arr[left]
                left += 1
        
        if minlen == float('inf'):
            return 0
        else:
            return minlen
        

if __name__ == "__main__":
    sol = Solution()

    # Input: 
    x = 51
    arr = [1, 4, 45, 6, 0, 19]
    # Output: 3

    print(sol.smallestSubWithSum(x,arr))