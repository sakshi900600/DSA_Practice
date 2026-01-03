class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        nge = [-1]*n
        st = [] #stack
        
        # put last elem in stack
        st.append(arr[-1])

        for i in range(n-2, -1, -1):
            curr = arr[i]
            
            while st and st[-1] <= curr:
                st.pop()
            
            if st:
                nge[i] = st[-1]
            
            st.append(curr)
                
                
        return nge
        



if __name__ == "__main__":
    sol = Solution()

    arr = [6,8,0,1,3]
    # Output: [8, -1, 1, 3, -1]
    print(sol.nextLargerElement(arr))