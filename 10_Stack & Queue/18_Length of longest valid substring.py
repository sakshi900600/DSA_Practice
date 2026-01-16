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
    # see inside else if st is empty then it means its invalid. So we are storing it so that we can find out the length. basically here we are using last_invalid_idx and stack top elem as boundaries so that we cant get length of valid substrings. 
     
    def maxLength2(self, s):
        # code here 
        n = len(s)
        last_invalid_idx = -1
        
        st = []
        maxLen = 0
        
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                if not st:
                    last_invalid_idx = i
                else:
                    st.pop()
                    if not st:
                        length = i - last_invalid_idx
                    else:
                        length = i - st[-1]
                    
                    maxLen = max(maxLen, length)
            
        return maxLen






            
            
            
        
if __name__ == "__main__":

    sol = Solution()
    # s = "(()("
    # output: 2

    # s = "()(())("
    # output: 6

    s = "()))((())()(("
    # output: 6

    # print(sol.isvalid(s))
    print(sol.maxLength(s))
    print(sol.maxLength2(s))
