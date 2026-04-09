# split array largest sum, painters partition and book allocation problem all are same just the language is changed.


class Solution:
    def minTime (self, arr, k):
        # code here
        si = max(arr)
        ei = sum(arr)
        
        while si <= ei:
            mid = (si+ei)//2
            painters = self.helper(arr,k,mid)
            
            if painters > k:
                si = mid+1
            else:
                ei = mid-1
        
        return si
        
        
    def helper(self, arr, k, time):
        n = len(arr)
        p = 1
        ballct = 0
        
        for i in range(n):
            
            if arr[i] + ballct <= time:
                ballct += arr[i]
            else:
                p += 1
                ballct = arr[i]
        
        return p
                


if __name__ == "__main__":
    sol = Solution()

    arr = [5, 10, 30, 20, 15]
    k = 3

    print(sol.minTime(arr,k))
    # Output: 35
    