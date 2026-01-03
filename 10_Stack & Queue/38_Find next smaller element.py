class Solution:
    def nextSmallerElement(self, arr):
        # code here
        n = len(arr)
        nse = [-1]*n
        st = [] #stack
        
        # put last elem in stack
        st.append(arr[-1])

        for i in range(n-2, -1, -1):
            curr = arr[i]
            
            while st and st[-1] >= curr:
                st.pop()
            
            if st:
                nse[i] = st[-1]
            
            st.append(curr)
                
                
        return nse
        



if __name__ == "__main__":
    sol = Solution()

    arr = [4, 8, 5, 2, 25]
    # Output: [2, 5, 2, -1, -1]
    print(sol.nextSmallerElement(arr))