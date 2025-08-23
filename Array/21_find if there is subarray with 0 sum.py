class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        ##Your code here
        #Return true or false
        prefix_sum = 0
        seen = set()
    
        for num in arr:
            prefix_sum += num
            if prefix_sum == 0 or prefix_sum in seen:
                return True
            seen.add(prefix_sum)
        
        
        return False
    

if __name__ == "__main__":
    sol = Solution()

    # input:
    arr = [4, 2, -3, 1, 6]

    # Output: true
    
    print(sol.subArrayExists(arr))