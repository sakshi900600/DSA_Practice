class Solution:
    def isPowerofTwo(self, n):
        # code here
        
        count = 0
        
        while n:
            n = n & (n-1)
            count += 1
        
        if count == 1:
            return True
        
        return False

    

if __name__ == "__main__":
    n = 16
    sol = Solution()
    print(sol.isPowerofTwo(n))

    # Output: True