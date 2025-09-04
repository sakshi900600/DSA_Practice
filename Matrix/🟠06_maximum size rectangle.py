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
        
                