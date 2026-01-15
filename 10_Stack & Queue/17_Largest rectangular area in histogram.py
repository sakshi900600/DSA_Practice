class Solution:
    def getMaxArea(self, arr):
        # code here
        
        n = len(arr)
        nse = [0]*n
        pse = [0]*n

        nse[n-1] = n
        pse[0] = -1
        st = []

        # next smaller elems
        st.append(n-1)
        for i in range(n-2, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if not st:
                nse[i] = n
            else:
                nse[i] = st[-1]
            
            st.append(i)

        # print(nse)

        # previous smaller elem
        st = []
        st.append(0)
        for i in range(1,n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if not st:
                pse[i] = -1
            else:
                pse[i] = st[-1]
            
            st.append(i)
        
        # print(pse)

        # maxarea calculation
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] -1
            area = arr[i] * width
            max_area = max(max_area, area)
        
        return max_area






if __name__ == "__main__":

    sol = Solution()
    arr = [60, 20, 50, 40, 10, 50, 60]
    # Output: 100
    
    # arr = [6, 4, 10, 3, 3, 8, 4, 10]
    # Output: 24

    print(sol.getMaxArea(arr))
