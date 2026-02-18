#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        # code here
        
        if (l<1 or r>32):
            return x
            
        for i in range(l,r+1):
            mask = 1 << (i-1)
            
            if (y & mask) != 0:
                x = x | mask
        
        return x
        
        
if __name__ == "__main__":
    x = 44
    y = 3
    l = 1
    r = 5
    
    sol = Solution()
    print(sol.setSetBit(x, y, l, r))

    # Output: 47
    