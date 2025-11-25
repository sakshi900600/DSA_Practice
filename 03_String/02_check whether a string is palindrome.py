class Solution:
    def isPalindrome(self, s):
        # code here
        si = 0
        ei = len(s)-1
        
        while si <= ei:
            if s[si] != s[ei]:
                return False
            si += 1
            ei -= 1
        
        return True
        


if __name__ == "__main__":

    sol = Solution()

    # Input:
    s = "abba"
    # Output: true

    print(sol.isPalindrome(s))