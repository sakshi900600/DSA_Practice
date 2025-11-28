class Solution:
    def reverse(self, s: str) -> str:
        #code here 
        
        st = []
        
        for ch in s:
            st.append(ch)
        
        ans = ""
        while st:
            ans += st.pop()
        
        
        return ans



if __name__ == "__main__":
    sol = Solution()

    s = "Sakshi"
    print(sol.reverse(s))
