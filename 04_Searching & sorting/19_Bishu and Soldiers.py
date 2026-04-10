# similar problem on gfg: https://www.geeksforgeeks.org/problems/killing-spree3020/1


#User function Template for python3

from math import sqrt
class Solution:

    # tle --------
    def killinSpree (self, n):
        # code here
        cnt = 0
        for i in range(1, int(sqrt(n))+1):
            x = (i*i)
            
            if n >= x:
                cnt += 1
                n -= x
            else:
                break
        
        return cnt
                

    # optimized
    def killinSpree_opt(self, n):
        # code here
        low = 0
        high = 10**12
        
        while low <= high:
            mid = (low+high)//2
            
            val = self.squareSeries(mid)
            
            if val <= n:
                ans = mid
                low = mid+1
            else:
                high = mid-1
        
        return ans
        
    
    def squareSeries(self, n):
        return (n*(n+1)*(2*n+1))//6
        



if __name__ == "__main__":
    sol = Solution()

    n = 14
    print(sol.killinSpree(n))
    print(sol.killinSpree_opt(n))

    # Output: 3
