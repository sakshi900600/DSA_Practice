
class Solution:
    def longestPalindrome(self, s):
        # code here
        n = len(s)
        
        longest =  float('-inf')
        ans = ""
        
        for i in range(n):
            for j in range(i,n):
                substr = s[i:j+1]
                
                if substr == substr[::-1]:
                    length = j-i+1
                    if length > longest:
                        longest = length
                        ans = substr
                        
        
        return ans
    

    