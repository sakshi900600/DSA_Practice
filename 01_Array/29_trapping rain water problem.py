
class Solution:
    def maxWater(self, arr):
        # code here
        
        n = len(arr)
        
        left_boundary = [-1]*n
        left_boundary[0] = arr[0]
        
        for i in range(1,n):
            left_boundary[i] = max(arr[i],left_boundary[i-1])
        
        
        right_boundary = [-1]*n
        right_boundary[n-1] = arr[n-1]
        
        for i in range(n-2,-1,-1):
            right_boundary[i] = max(arr[i],right_boundary[i+1])
            
        
        water_level = [-1]*n
        trapped_water = 0
        
        for i in range(n):
            water_level[i] = min(right_boundary[i], left_boundary[i])
            trapped_water += water_level[i] - arr[i]
            
            
        return trapped_water
            
            

if __name__ == "__main__":
    sol = Solution()

    # Input: 
    arr = [3, 0, 1, 0, 4, 0 ,2]
    # Output: 10
    print(sol.maxWater(arr))