class Solution:
    
    #xplaination:  look we are tracking prefix sum using a set and we are checking prefix_sum in seen.
    # - why checking in set:   look we are finding sum so as we move forward the sum should become larger right. And if sum is same as any previous sum then it means where we previously get the sum and where we are getting that same sum again , in between of that sum is 0.
    # so subarry with 0 sum does exists.

    
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