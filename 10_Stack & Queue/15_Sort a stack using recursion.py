class Solution:

    def sortStack(self, st):
        # code here 
        temp_st = []
        
        while st:
            if len(temp_st) == 0:
                temp_st.append(st.pop())
            
            else:
                if temp_st and st[-1] >= temp_st[-1]:
                    temp_st.append(st.pop())
                else:
                    elem = st.pop()
                    while temp_st and temp_st[-1] > elem:
                        st.append(temp_st.pop())
                    temp_st.append(elem)
        
        st[:] = temp_st
        return st


    # sort a stack using recursion
    def sortStack_rec(self, st):
        # code here 
        if len(st) == 0:
            return
        
        elem = st.pop()
        self.sortStack(st)
        self.insertElem(st, elem)
        
        return st
        
    
    def insertElem(self,st, x):
        if len(st) == 0:
            st.append(x)
        
        else:
            
            if st[-1] <= x:
                st.append(x)
            else:
                elem = st.pop()
                self.insertElem(st,x)
                st.append(elem)
        
        return st
        



if __name__ == "__main__":
    st = [34, 3, 31, 98, 92, 23]
    # output:  [3, 23, 31, 34, 92, 98]

    # st = [1,2,3]
    # output: [1,2,3] - already sorted

    sol = Solution()
    # sorted_stack = sol.sortStack(st)
    sorted_stack = sol.sortStack_rec(st)
    print("Sorted Stack:", sorted_stack)