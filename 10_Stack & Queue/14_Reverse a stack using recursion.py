class Solution:
    def reverseStack(self, st):
        # code here
        
        # with extra space
        # aux_st = []
        # while st:
        #     aux_st.append(st.pop())
        
        # st[:] = aux_st
        
        # return st
        
        
        # without extra space
        if not st:
            return
        
        top = st.pop()
        self.reverseStack(st)
        self.insertAtBottom(st,top)
        
        return st
        
        
        
    
    def insertAtBottom(self, st, x):
        if len(st) == 0:
            st.append(x)
        else:
            top = st[-1]
            st.pop()
            self.insertAtBottom(st,x)
            st.append(top)
        
        return st



if __name__ == "__main__":
    st = [1, 2, 3, 4, 5]
    obj = Solution()
    res = obj.reverseStack(st)
    print(res)

    # Ouptput: [5, 4, 3, 2, 1]