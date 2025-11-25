class Solution(object):

    # correct but tle: 
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        for i in range(n):
            leftsum = 0
            rightsum =0 

            idx = i-1

            while idx >= 0:
                leftsum += nums[idx]
                idx -= 1
            
            idx = i+1
            while idx < n:
                rightsum += nums[idx]
                idx += 1

            
            if leftsum == rightsum:
                return i

        return -1


    # this approach works:
    # see in an array if we want sum from any index i+1 to n(call it rightsum) then we can get it as:  totalSum - sum(0,i)(call it leftsum).

    # here we applied same approach. 
    # so for the left part we can add elem as we traversing the array and for the right sum we will apply that formula. but remember in leftsum it stores sum till i-1th index and according to the formula we need to sub sum till ith index so doing -a[i]. At last compare if same then return index otherwise -1.

    def pivotIndex_opt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0

        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1   
        


if __name__ == "__main__":
    sol = Solution()

    # input:
    a = [1,7,3,6,5,6]

    # output: 3
    # print(sol.pivotIndex(a))
    print(sol.pivotIndex_opt(a))