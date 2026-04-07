
class Solution:

    # using linear search

    def findPages(self, arr, k):
        # code here
        n = len(arr)
        
        if k > n:
            return -1
        
        si = max(arr)
        ei = sum(arr)
        
        for pages in range(si, ei+1):
            std = self.helper(arr,pages)
            
            if std <= k:
                return pages
        
        return -1
    
    
    def helper(self, arr, pages):
        n = len(arr)
        std = 1
        page_allct = 0
        
        for i in range(n):
            if page_allct + arr[i] <= pages:
                page_allct += arr[i]
            else:
                std += 1
                page_allct = arr[i]
        
        return std
        

    # using binary search
    def findPages_bs(self, arr, k):
        # code here
        n = len(arr)
        
        if k > n:
            return -1
        
        si = max(arr)
        ei = sum(arr)
        
        while si <= ei:
            mid = (si+ei)//2
            
            std = self.helper(arr,mid)
            
            if std > k:
                si = mid+1
            else:
                ei = mid-1
        
        return si
    


if __name__ == "__main__":
    sol = Solution()

    arr = [12, 34, 67, 90]
    k = 2

    print(sol.findPages(arr,k))
    print(sol.findPages_bs(arr,k))
    # Output: 113
