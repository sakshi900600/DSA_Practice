#User function Template for python3

class Solution:
    def findPosition(self, n):
        # code here 
        total1 = 0
        setpos = -1
        i = 1
        
        while n>0:
            if (n&1):
                total1 += 1
                setpos = i
            
            if total1 > 1:
                return -1
            
            n = n >> 1
            i += 1
        
        
        return setpos



if __name__ == "__main__":
    n = 16
    sol = Solution()
    print(sol.findPosition(n))

    # Output: 5

    