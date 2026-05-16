# In last ques there were no duplicates so simply getting min from left or right was working, but here we have duplicates as well so that condition fails here. 

# here we will use ei for comparisions, coz in a rotated sorted array, the minimum element lies in the "unsorted break". Comparing with ei helps identify that break cleanly. 

# if mid and end are same then we can not decide which side to go so we will just reduce the end by 1 and check again.



class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        si = 0
        ei = n-1
        ans = float('inf')

        while si < ei:
            mid = (si+ei)//2

            if nums[mid] < nums[ei]:
                ans = min(ans, nums[mid])
                ei = mid
            elif nums[mid] > nums[ei]:
                ans = min(ans, nums[ei])
                si = mid+1
            else:
                ei -= 1
        
        return ans



if __name__ == "__main__":
    nums = [10,1, 10, 10, 10]
    # nums = [2,2,2,0,1]
    sol = Solution()

    print(sol.findMin(nums))

    # Output: 1