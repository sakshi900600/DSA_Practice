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
            
        


if __name__ == "__main__":
    sol = Solution()

    # input:
    a = [1,7,3,6,5,6]

    # output: 3
    print(sol.pivotIndex(a))