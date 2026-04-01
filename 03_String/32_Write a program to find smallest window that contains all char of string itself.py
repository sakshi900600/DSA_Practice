#User function Template for python3

class Solution:
    def findSubString(self, s):
        # code here
        n = len(s)
        uniqch = len(set(s))
        minlen = float("inf")
        freq = [0]*26
        
        currch = 0
        i = 0
        
        for j in range(n):
            idx = ord(s[j])-ord('a')
            
            if freq[idx]==0:
                currch += 1
            
            freq[idx] += 1
            
            while currch == uniqch:
                minlen = min(minlen, j-i+1)
                
                idxi = ord(s[i])-ord('a')
                
                freq[idxi] -= 1
                if freq[idxi] == 0:
                    currch -= 1
                
                i += 1
        
        return minlen
    
    
if __name__ == "__main__":
    sol = Solution()

    s = "aabcbcdbca"
    print(sol.findSubString(s))
    # Output: 4
