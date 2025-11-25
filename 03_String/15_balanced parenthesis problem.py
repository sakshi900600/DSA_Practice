class Solution:

    # approach-1 using stack.
    def isBalanced(self, s):
        # code here
        
        n = len(s)
        st = [] # stack
        
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)
            else:
                if len(st) == 0:
                    return False
                    
                else:
                    # matching
                    if (ch==')' and st[-1]=='(') or (ch=='}' and st[-1]=='{') or (ch==']' and st[-1]=='['):
                        st.pop()
                    else:
                        return False
                        
        
        return not st # if stack empty then false else true.
        

    # approach -2 replacing
    def is_Balanced(self, s):
        # code here
        
        n = len(s)
        
        while '()' in s or '{}' in s or "[]" in s:
            s = s.replace('()', "")
            s = s.replace('[]', "")
            s = s.replace('{}', "")
            
        
        if len(s) == 0:
            return True
            
        else:
            return False
        
    
        
    
if __name__ == "__main__":
    sol = Solution()

    # Input: 
    s = "[{()}]"
    # Output: true


    s = "([{]})"
    # Output: false

    # print(sol.isBalanced(s))
    # print(sol.is_Balanced(s))