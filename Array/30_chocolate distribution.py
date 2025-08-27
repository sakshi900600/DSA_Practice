#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):

        # code here
        n = len(arr)
        
        if M==0 or n==0:
            return 0
        
        if M > n:
            return -1
        
        arr.sort()
        
        minDiff = float('inf')
        
        for i in range(n-M+1):
            currDiff = arr[i+M-1] - arr[i]
            if currDiff < minDiff:
                minDiff = currDiff
        
        
        return minDiff
        



if __name__ == "__main__":
    sol = Solution()

    # Input: 
    arr = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5
    # Output: 6

    print(sol.findMinDiff(arr,m))