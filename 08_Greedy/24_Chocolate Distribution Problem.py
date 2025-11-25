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
        mindiff = float('inf')
    
        for start in range(len(arr)-M+1):
            end = start + M -1
            diff = arr[end] - arr[start]
            mindiff = min(diff, mindiff)
        
        return mindiff
        
              

if __name__ == '__main__':
    sol = Solution()

    # input:
    arr = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5

    # Output: 6
    print(sol.findMinDiff(arr, m))