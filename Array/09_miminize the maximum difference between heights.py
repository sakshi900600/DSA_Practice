class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        
        if n == 0 or n==1:
            return 0
            
        arr.sort()

        mindiff = arr[-1] - arr[0]
        small = arr[0]+k
        large = arr[n-1]-k

        if small > large:
            small,large = large,small
        
        for i in range(n-1):
            left_add = arr[i]+k
            right_sub = arr[i+1]-k

            if right_sub < 0:
                continue

            curr_min = min(small, right_sub)
            curr_max = max(large, left_add)
            mindiff = min(mindiff, curr_max-curr_min)

        
        return mindiff
        


if __name__ == '__main__':

    sol = Solution()

    # input:
    arr = [3, 9, 12, 16, 20]
    k = 3
    # output: 11
    
    print(sol.getMinDiff(arr,k))