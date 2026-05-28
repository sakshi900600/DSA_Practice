class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        l = 0
        r = n-1
        s = list(s)

        while l < r:
            if not s[l].isalpha():
                l +=  1
            elif not s[r].isalpha():
                r -= 1
            else:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        
        return "".join(s)
        
        