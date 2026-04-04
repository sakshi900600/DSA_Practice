class Solution:

    # Brute force approach: check for longest palindromic prefix(k) and the rest no of char we will need to add to make the full string a plaindrom which is (n-k)

    def minChar(self, s):
        # code here
        
        n = len(s)
        longpldrm = self.longPalindrome(s)
        
        return n - longpldrm
        
    # finding this takes lots of time so TLE ---------------
    def longPalindrome(self,s):
        longest = 0
        n = len(s)
        
        for i in range(n):
            temp = s[0:i+1]
            if temp == temp[::-1]:
                longest = i+1
                
                
        return longest
        

    # optimized using lps array
    def minChar_opt(self, s):
        # code here
        
        n = len(s)
        revs = s[::-1]
        temp = s + "$" + revs
        
        longpldrm = self.lps(temp)
        
        return n - longpldrm
        
    
    def lps(self,pat):
        m = len(pat)
        
        lps = [0]*m
        
        length = 0
        i = 1
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            
            else:
                if length > 0:
                    length = lps[length-1]
                
                else:
                    lps[i] = 0
                    i += 1
        
        return lps[-1]
            
        
        
if __name__ == "__main__":
    sol = Solution()

    s = "cxggbw"
    print(sol.minChar(s))
    print(sol.minChar_opt(s))

    # output: 5

    