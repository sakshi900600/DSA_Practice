# in any expression we use brackets so that we can do any calculation, but if there is no calculation then it means its redundant


class Solution():
    def checkRedundancy(self, s):
        # code here 
        n = len(s)
        st = []
        operators = ['+', '-', '*', '/']
        
        for i in range(n):
            if s[i] != ')':
                st.append(s[i])
            else:
                op = 0
                while st[-1] != '(':
                    top = st[-1]
                    if top in operators:
                        op += 1
                    st.pop()
                
                if op == 0:
                    return True
                st.pop()
        
        return False
                    



if __name__ == "__main__":
    sol = Solution()

    # input;
    s = "((a+b))"
    # output: True
    s = "((a+b)*c)"
    # output: False

    print(sol.checkRedundancy(s))