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
                

