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
        

def choco_dis(arr, m):
    # first sort the array so that the min val will be in start and max at end of the windown of m size.
    # now every time we need to create m size window so we need to find out how many windows we can create ?
    # len(a) - m + 1: 
    # start will be i and end will be a[i+m-1]
    # find diff and store mindiff

    arr.sort()
    mindiff = float('inf')

    for start in range(len(arr)-m+1):
        end = start + m -1
        diff = arr[end] - arr[start]
        mindiff = min(diff, mindiff)
    
    return mindiff


if __name__ == "__main__":
    sol = Solution()

    # Input: 
    arr = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5
    # Output: 6

    print(sol.findMinDiff(arr,m))
    print(choco_dis(arr, m))