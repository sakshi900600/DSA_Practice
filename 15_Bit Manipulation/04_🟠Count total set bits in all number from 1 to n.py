class Solution:

    # Tle----------
    def countSetBits(self,n):
        # code here
        
        count = 0
        for i in range(1,n+1):
            count += self.csb_for1_num(i)
        
        return count
        
        
    def csb_for1_num(self, n):
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        
        return count    
     


if __name__ == "__main__":
    n = 6
    sol = Solution()
    print(sol.countSetBits(n))

    # Output: 9

