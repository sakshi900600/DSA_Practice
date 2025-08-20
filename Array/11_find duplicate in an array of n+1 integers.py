class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # tle: ---------------

        n = len(nums)

        # for i in range(1,n+1):
        #     if i in nums:
        #         nums.remove(i)
        
        # return nums[0]


        # We will treat arr as linked list and apply cycle detection logic in it

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        

        return slow
        



if __name__ == '__main__':

    sol = Solution()

    # input:
    arr = [1,3,4,2,2]
    # output: 2
    
    print(sol.findDuplicate(arr))