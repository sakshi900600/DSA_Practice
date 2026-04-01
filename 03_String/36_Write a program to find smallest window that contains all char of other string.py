class Solution:
    def minWindow(self, s, p):
        # code here
        
        dct1 = {}
        for ch in p:
            dct1[ch] = dct1.get(ch,0)+1
        
        uniqch = len(set(p))
        currch = 0
        
        n = len(s)
        dct2 = {}
        minlen = float("inf")
        ans = ""
        
        i = 0
        for j in range(n):
            
            if s[j] in dct1:
                dct2[s[j]] = dct2.get(s[j],0)+1
            
                if dct1[s[j]] == dct2[s[j]]:
                    currch += 1
            
            
            while currch == uniqch:
                length = j-i+1
                if length < minlen:
                    minlen = length
                    ans = s[i:j+1]
                
                if s[i] in dct2:
                    dct2[s[i]] -= 1
                
                    if dct2[s[i]] < dct1[s[i]]:
                        currch -= 1
                
                i += 1
        
        return ans
        
        
                    
if __name__ == "__main__":
    sol = Solution()

    s = "timetopractice"
    p = "toc"
    print(sol.minWindow(s,p))

    # Output: "toprac"
                   
                       
            