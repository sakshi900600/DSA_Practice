class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        
        if n == 1:
            return 0
            
        arr.sort()
        # initial_difference....
        ans = arr[-1] - arr[0]
        
        mini = arr[0]+k
        maxi = arr[-1]-k
        
        
        for i in range(1,n):
            
            if arr[i]-k < 0:
                continue
            
            curr_min = min(mini, arr[i]-k)
            curr_max = max(maxi, arr[i-1]+k)
            
            
            ans = min(ans, curr_max-curr_min)
        
        
        return ans
            


if __name__ == '__main__':

    sol = Solution()

    # input:
    arr = [3, 9, 12, 16, 20]
    k = 3
    # output: 11
    
    print(sol.getMinDiff(arr,k))