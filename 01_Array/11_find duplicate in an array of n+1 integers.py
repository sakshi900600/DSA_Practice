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
        

    # this approach gives wrong ans for many outputs.
    def find_duplicate(self,arr):
        slow = 0
        fast = 1
        n = len(arr)

        while True:
            slow += 1
            fast += 2
            
            if slow == n:
                slow = 0
            if fast==n:
                fast = 0
            if fast==n+1:
                fast = 1

                
            if arr[slow] == arr[fast]:
                return arr[slow]

        return -1
            

    # another approach:  we will reach at each index and then we will mark that value negative .
    def mark_duplicate(self, arr):
        for i in range(len(arr)):
            idx = abs(arr[i]) # taking pos value as index
            if arr[idx] < 0: # if already negative , then we found duplicate
                return idx
            else: # marking value as negative
                arr[idx] = - arr[idx]
        return -1

    


if __name__ == '__main__':

    sol = Solution()

    # input:
    arr = [1,3,4,2,2]
    # output: 2
    
    # print(sol.findDuplicate(arr))
    # print(sol.find_duplicate(arr))
    print(sol.mark_duplicate(arr))