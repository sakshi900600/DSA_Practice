class Solution:

    # tle ----------
    def maxLength(self, s):
        # code here 
        
        # brute force
        n = len(s)
        longest = 0
        
        for i in range(n):
            for j in range(i+1,n):
                substr = s[i:j+1]
                
                if self.isvalid(substr):
                    length = j-i+1
                    longest = max(longest, length)
        
        return longest        
    
    def isvalid(self, s):
        st = []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                st.append(s[i])
            else:
                if not st:
                    return False
                
                if s[i] == ')' and st[-1] == '(':
                    st.pop()
        
        return not st
            
    
    # optimized ----------
    def maxLength(self, s):
        # code here 
        
        # optimized
        n = len(s)
        
        st = []
        maxLen = 0
        
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                if len(st) > 0:
                    topidx = st.pop()
                    length = i-topidx+1
                    maxLen = max(maxLen, length)
            
        return maxLen


    

            
            
            
        
if __name__ == "__main__":

    sol = Solution()
    s = "(()("
    # output: 2

    s = "()(())("
    # output: 6

    s = "()))((())()(("
    # output: 6

    # print(sol.isvalid(s))
    print(sol.maxLength(s))
