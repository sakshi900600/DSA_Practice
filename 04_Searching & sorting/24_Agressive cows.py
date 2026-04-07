class Solution:
    # linear search approach: 
    def aggressiveCows(self, stalls, k):
        # code here
        n = len(stalls)
        stalls.sort()
        
        maxi = max(stalls)
        mini = min(stalls)
        
        for i in range(1, maxi-mini):
            if self.ispossible(stalls,i,k):
                continue
            else:
                return i-1
        
        return maxi-mini
        
    
    def ispossible(self, arr,dist,k):
        n = len(arr)
        cowcnt = 1
        last = arr[0]
        
        for i in range(1,n):
            if arr[i]-last >= dist:
                cowcnt += 1
                last = arr[i]
                
                if cowcnt == k:
                    return True
        
        return False
    

    # binary search approach:
    def aggressiveCows_bs(self, stalls, k):
        # code here
        n = len(stalls)
        stalls.sort()
        
        si = 1
        ei = stalls[-1]-stalls[0]
        
        ans = -1
        
        while si <= ei:
            mid = (si+ei)//2
            
            if self.ispossible(stalls,mid,k):
                ans = mid
                si = mid+1
            else:
                ei = mid-1
        
        return ans



if __name__ == "__main__":
    sol = Solution()

    arr = [1, 2, 4, 8, 9]
    k = 3
    print(sol.aggressiveCows(arr,k))
    print(sol.aggressiveCows_bs(arr,k))

    # Output: 3
