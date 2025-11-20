class Solution:
    def palinParts (self, s):
        # code here
        
        ans = []
        n = len(s)
        
        def helper(idx, curr):
            if idx == n:
                ans.append(curr[:]) # add copy of curr in ans
                return
            
            for j in range(idx+1, n+1):
                substr = s[idx: j]
                if substr == substr[::-1]:
                    curr.append(substr)
                    helper(j, curr)
                    curr.pop()
        
        helper(0, [])
        
        return ans


# Dobut soln:  why ans.append(curr[:]) work but ans.append(curr) not ?
# ans.append(curr) - adds reference of curr in ans.
# ans.append(curr[:]) - adds copy of curr in ans.

# Now due to backtracking substr are being added and removed from curr. so at the end curr is empty and thats why simply appending curr doesn't work. so we store copy of curr when idx == n.

# Chamak gaya 💫✨🌟



if __name__ == "__main__":
    sol = Solution()

    # Input:
    s = "geeks"
    print(sol.palinParts(s))

    # Output:
    # [['g', 'e', 'e', 'k', 's'], ['g', 'ee', 'k', 's']]