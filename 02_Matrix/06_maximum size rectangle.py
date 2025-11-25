class Solution:

    # next smaller element:
    def next_smaller(self, a):
        n = len(a)
        nexts = [-1]*n
        st = []

        st.append(n-1)

        for i in range(n-2,-1,-1):
            while st and a[st[-1]] > a[i]:
                st.pop()

            if len(st) != 0:
                nexts[i] = st[-1]
            else:
                nexts[i] = n

            # st.append(a[i])
            st.append(i)

        return nexts


    # previous smaller element:
    def prev_smaller(self, a):
        n = len(a)

        prevs = [-1]*n
        st = []
        st.append(0)

        for i in range(1,n):
            while st and a[st[-1]] > a[i]:
                st.pop()
            
            if len(st) != 0:
                prevs[i] = st[-1]
            else:
                prevs[i] = -1
            
            # st.append(a[i])
            st.append(i)
        
        return prevs


    # largest rectangle in histogram:
    def larg_rec_histo(self,heights):
        # store prevs and nexts index instead of value. So that we can find out width.
        nexts = self.next_smaller(heights)
        prevs = self.prev_smaller(heights)

        max_area = 0
        n = len(heights)

        for i in range(n):
            width = nexts[i] - prevs[i]-1
            area = heights[i]*width
            max_area = max(area, max_area)

        return max_area
    





def histogram_opt(a):
    max_area = 0
    st = [] # stack
    a = a +[0]

    n = len(a)
    i = 0
    while i<n:
        if not st or (a[i] >= a[st[-1]]):
            st.append(i)
            i += 1
        else:
            top = st.pop()
            height = a[top]

            if not st:
                width = i
            else:
                width = i-st[-1]-1
            
            area = height * width
            # print(area)

            max_area = max(max_area,area)
    
    return max_area



def largest_rectangle(mat):
    row = len(mat)
    col = len(mat[0])
    max_area = float('-inf')
    
    h = [0]*col

    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                h[j] += 1
            else:
                h[j] = 0
        
        max_area = max(max_area, histogram_opt(h))

    # print(h)
    return max_area




if __name__ == "__main__":
    sol = Solution()

    # input:
    # a = [3,5,1,7,9]

    # next smaller element:
    # [1,1,-1,-1,-1] - elements
    # [1, 2, -1, -1, -1]  - index
    # print(sol.next_smaller(a))
    

    # prev smaller element:
    # [-1,3,-1,1,7] - elements
    # [-1, 3, 1, 2, 3] - index
    # print(sol.prev_smaller(a))
                

    # largest rectangel in histogram:
    # a = [3,5,1,7,5,9]
    # output: 15
    # print(sol.larg_rec_histo(a))




mat = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
print(largest_rectangle(mat))