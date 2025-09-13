class Solution:
    def maxArea(self, mat):
        # Your code here
        n = len(mat)
        m = len(mat[0])
        
        li = []
        
        for i in range(n):
            sum = 0
            for j in range(m):
                sum += mat[i][j]
            
            li.append(sum)
        
        # print(li)
        
        # now its similar like largest rectangle in histogram
        
        return self.largest_rec_histogram(li)
        
        
    
    def largest_rec_histogram(self,heights):
        
        n = len(heights)
        maxArea = 0
        
        
        for i in range(n):
            minh = heights[i]
            
            for j in range(i,n):
                minh = min(minh, heights[j])
                width = j-i+1
                
                area = minh * width
                maxArea = max(maxArea, area)
                
        return maxArea
                
        
    # I dry run this code on an example and it doesn't work 🥲.
        




    # for histogram width calculation you want:
    # next[i] = n if no smaller element exists on the right,
    # prev[i] = -1 if no smaller element exists on the left.



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
    a = [3,5,1,7,5,9]
    # output: 15
    print(sol.larg_rec_histo(a))