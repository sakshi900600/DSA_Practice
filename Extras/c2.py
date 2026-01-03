# 2. Maximum Sum of Three Numbers Divisible by Three

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # max_sum = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1,n):
        #             sum = nums[i] + nums[j] + nums[k]
        #             if sum % 3 == 0:
        #                 max_sum = max(sum, max_sum)


        # recursion
        max_sum = [0]
        def maxSumHelper(idx, maxSum, sum, count):
            if idx > n:
                return
            
            if idx == n: 
                if count == 3 and sum %3==0:
                    maxSum[0] = max(maxSum[0], sum)
                return
            if count == 3:
                if sum % 3 == 0:
                    maxSum[0] = max(maxSum[0], sum)
                return 
            
            # pick
            maxSumHelper(idx+1, maxSum, sum+nums[idx], count+1)
            maxSumHelper(idx+1, maxSum, sum, count)
        

        maxSumHelper(0, max_sum, 0, 0)
        return max_sum[0]
    
    
    


if __name__ == '__main__':

    sol = Solution()

    nums = [4,2,3,1]
    # output: 9
    # nums = [2,1,5]
    # Output: 0
    # nums = [8,7,4,3]
    # Output: 18
    print(sol.maximumSum(nums))