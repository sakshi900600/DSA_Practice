class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        si = 0
        ei = len(s)-1

        while si <= ei:
            s[si],s[ei] = s[ei],s[si]
        
            si += 1
            ei -= 1
        


if __name__ == "__main__":

    sol = Solution()

    # Input:
    s = ["h","e","l","l","o"]
    # Output: ["o","l","l","e","h"]

    sol.reverseString(s)
    print(s)