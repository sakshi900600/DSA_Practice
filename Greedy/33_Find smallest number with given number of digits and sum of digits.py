#User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        # code here
        
        # if sum doesn't lie in range
        if s < 1 or s > d*9:
            return "-1"
        
        
        li = ['0']*d
        # reverse 1 for the first position
        s -= 1
        
        for i in range(d-1, 0,-1):
            if s > 9:
                li[i] = '9'
                s -= 9
            else:
                li[i] = str(s)
                s = 0
        
        # add the remaining s at 0th idx
        li[0] = str(1 + s)
        
        return ''.join(li)
        
        
        
if __name__ == '__main__':
    sol = Solution()
    s = 9
    d = 2

    # Output: 18
    print(sol.smallestNumber(s, d))