#User function Template for python3

class Solution:
    def wordBreak(self, dct, s):
        # code here
        n = len(s)
        ans = []
        
        def helper(idx, curr):
            if idx == n:
                ans.append(" ".join(curr))
                return
            
            for j in range(idx+1, n+1):
                word = s[idx: j]
                if word in dct:
                    curr.append(word)
                    helper(j, curr)
                    curr.pop()
            
        helper(0, [])
        
        return ans
    


if __name__ == "__main__":
    sol = Solution()

    # Input:
    s = "likegfg"
    dct = ["lik", "like", "egfg", "gfg"]

    print(sol.wordBreak(dct,s))
    # Output: ['lik egfg', 'like gfg']