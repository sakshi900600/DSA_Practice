#User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self,s):
        # code here 
        
        # store opening position
        pos_open = []
        for i in range(len(s)):
            if s[i] == "[":
                pos_open.append(i)
                
        count = 0
        pos = 0
        ans = 0
        # converting into list coz string is immutable
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == '[':
                count += 1
                pos += 1 # means this opening will not be used
            else:
                count -= 1
            
            if count < 0:
                # swaps = pos of [ - post of ]
                ans += pos_open[pos] - i
                s[i],s[pos] = s[pos],s[i]
                
                # reset
                pos += 1
                count = 1 # coz the opening used for swap is counted
                
                
        return ans
        
        