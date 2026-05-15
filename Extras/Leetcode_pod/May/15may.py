class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(arr)
        si = 0
        ei = n-1
        ans = float('inf')

        while si <= ei:
            mid = (si+ei)//2

            if arr[si] <= arr[mid]:
                ans = min(arr[si], ans)
                si = mid+1
            else:
                ans = min(arr[mid], ans)
                ei = mid-1
        
        return ans
    

    