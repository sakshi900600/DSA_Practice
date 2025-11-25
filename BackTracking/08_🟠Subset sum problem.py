
# TLE ------------------
class Solution:
    def equalPartition(self, arr):
        # code here
        n = len(arr)
        
        if n == 1:
            return False
        
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return False
        
        req_sum = total_sum // 2
        
        def helper(idx, csum):
            if csum == req_sum:
                return True
            
            if idx == n or csum > req_sum:
                return False
            
            
            if helper(idx+1, csum+arr[idx]):
                return True
            
            if helper(idx+1, csum):
                return True
            
            return False
        
        
        return helper(0,0)
            
        
        

if __name__ == "__main__":
    arr = [9,9,10,8,4,8]
    arr = [5,3,2,2]
    sol = Solution()

    # Output: False
    print(sol.equalPartition(arr))
