#User function Template for python3
class Solution:
    def insertAtBottom(self,st,x):
        # code here
        
        # with extra space;  
        # aux_st = []
        
        # while st:
        #     aux_st.append(st.pop())
        
        # st.append(x)
        
        # while aux_st:
        #     st.append(aux_st.pop())
        
        # return st
        
        
        # without extra space;
        if len(st) == 0:
            st.append(x)
        else:
            top = st[-1]
            st.pop()
            self.insertAtBottom(st, x)
            st.append(top)
        
        return st
        


if __name__ == "__main__":
    st = [1, 2, 3, 4]
    x = 0
    obj = Solution()
    res = obj.insertAtBottom(st, x)
    print(res)

    # Output: [0, 1, 2, 3, 4]