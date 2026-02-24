class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        
        if len(s1) != len(s2):
            return False
        
        dct1 = {}
        dct2 = {}
        
        for i in range(len(s1)):
            ch1 = s1[i]
            ch2 = s2[i]
            
            # char from s1 --> s2
            if ch1 not in dct1:
                dct1[ch1] = ch2
            else:
                if dct1[ch1] != ch2:
                    return False
            
            # char from s2 --> s1
            if ch2 not in dct2:
                dct2[ch2] = ch1
            else:
                if dct2[ch2] != ch1:
                    return False
        
        return True
            
            
            
if __name__ == "__main__":
    sol = Solution()

    s1 = "aab"
    s2 = "xxy"
    print(sol.areIsomorphic(s1,s2))
    # Output: True

    s1 = "aab"
    s2 = "xyz"
    print(sol.areIsomorphic(s1,s2))
    # Output: False

    