class Solution:
    def validateOp(self, a, b):
        # code here 
        n = len(a)
        j = 0
        
        st = []
        
        for i in range(n):
            st.append(a[i])
            
            while st and st[-1] == b[j]:
                st.pop()
                j += 1
            
        
        return j == len(b)
        
        

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [2, 1, 3]
    
    obj = Solution()
    print(obj.validateOp(a, b))

    # Output: True