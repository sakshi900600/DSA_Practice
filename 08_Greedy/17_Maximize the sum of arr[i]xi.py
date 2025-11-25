#User function Template for python3

class Solution:
    def maxValue(self, arr): 
        # Complete the function
        
        mod = 1000000007
        
        arr.sort()
        max_sum = 0
        
        for i in range(len(arr)):
            max_sum += arr[i]*i
        
        
        return max_sum % mod
      


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]

    # Output: 40
    print(sol.maxValue(arr))  
