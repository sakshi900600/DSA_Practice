#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        n = len(s)
        ans = []
        
        def helper(pos, visited, currStr):
            if len(currStr) == n:
                ans.append(currStr)
                return
            
            for i in range(n):
                if visited[i] == 0:
                    visited[i] = 1
                    helper(pos+1, visited, currStr+s[i])
                    visited[i] = 0
                
                
        visited = [0]*n
        helper(0,visited, "")
        
        ansSet = set(ans)
        final_ans = []
        
        for it in ansSet:
            final_ans.append(it)
            
        return final_ans
        


if __name__ == "__main__":
    sol = Solution()

    s = "ABC"
    print(sol.findPermutation(s))

    # Output: 
    # ['ABC', 'BCA', 'BAC', 'CBA', 'ACB', 'CAB']