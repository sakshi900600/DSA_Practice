#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        ans = ""
        ans += s[0]
        
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                continue
            else:
                ans += s[i]
        
        return ans
        
        

if __name__ == "__main__":
    sol = Solution()

    s = "aabb"
    print(sol.removeConsecutiveCharacter(s))
    # Output: ab

