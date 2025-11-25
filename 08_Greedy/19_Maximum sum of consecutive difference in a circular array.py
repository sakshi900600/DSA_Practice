#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        
        arr.sort()
        n = len(arr)
        
        new_a = [0]*n
        idx = 0
        for i in range(n//2):
            new_a[idx] = arr[i]
            new_a[idx+1] = arr[n-1-i]
            
            idx += 2
        
        if n % 2 != 0:
            new_a[-1] = arr[n//2]
        
        
        max_sum = 0
        for i in range(n-1):
            max_sum += abs(new_a[i]- new_a[i+1])
        
        
        # for last elem
        max_sum += abs(new_a[-1] - new_a[0])
        
        return max_sum
        
        
        
            
if __name__ == '__main__':
    sol = Solution()
    arr = [4,2,1,8]

    # Output: 18
    print(sol.maxSum(arr))