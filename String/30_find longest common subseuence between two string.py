class Solution:
    def lcs(self, s1, s2):
        # code here
        
        n = len(s1)
        m = len(s2)
        
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        row = m+1
        col = n+1
        
        for i in range(1, row):
            for j in range(1,col):
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        
        return dp[m][n]
        

if __name__ == "__main__":
    sol = Solution()

    # Input: 
    s1 = "XYZW"
    s2 = "XYWZ"
    # Output: 3

    print(sol.lcs(s1,s2))