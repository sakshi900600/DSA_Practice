class Solution:

    # 1st approach:  TLE 
    def kthSmallest(self, mat, k):
        # code here
        
        n = len(mat)
        m = len(mat[0])
        
        li = []
        
        for i in range(n):
            for j in range(m):
                li.append(mat[i][j])
                
        
        li.sort()
        return self.helper(li,k)
        
    
    def helper(self,arr,k):
        mini = arr[0]
        
        for i in range(k):
            mini = min(arr)
            arr.remove(mini)
        
        return mini
        
        
    
    # 2nd approach: 
    # I thought to keep min of right and bottom everytime but i saw an example where this approach doesn't work 🥲.

    def kthSmallest2(self, mat, k):
        # code here
        
        n = len(mat)
        m = len(mat[0])
        
        small = mat[0][0]
        
        i = 0
        j = 0 
        elem = mat[i][j]
        k -= 1
        
        while i<n and j<m:
            
            if j+1 < m:
                right = mat[i][j+1]
            
            if i+1< n:
                bottom = mat[i+1][j]
                
            small = min(right,bottom)
            k -= 1
            
            if k == 0:
                break
            
            elem = small
            
                    
        
        
        return small
    
      
    

    