#User function Template for python3

class Solution:
    def inSequence(self, a, b, c):
        # code here
        
        # formula => a + (n-1)*d
        # b = a + (n-1)*d
        # n = (b-a)/d + 1

        # in order to come b in the series.
        # 1. b-a should be divisible by d
        # 2. (b-a)/d it value must be >=0 . so that n always remain +ve.
        
        
        # if difference is 0
        if c == 0:
            return a==b
            
        c1 = (b-a)%c == 0
        c2 = (b-a)//c >= 0
        
        
        return c1 and c2
        



if __name__ == "__main__":
    sol = Solution()

    # input:
    a = 1
    b = 3
    c = 2
    # Output: true

    print(sol.inSequence(a,b,c))