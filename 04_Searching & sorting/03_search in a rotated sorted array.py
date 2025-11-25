
def rotated_search(nums,target):

    n = len(nums)

    si = 0
    ei = n-1

    while si <= ei:
        mid = (si+ei)//2

        if nums[mid] == target:
            return mid
        
        # left part sorted:
        if nums[si] <= nums[mid]:
            if nums[si] <= target <= nums[mid]:
                ei = mid-1
            else:
                si = mid+1
        
        # right part sorted 
        else:
            if nums[mid] <= target <= nums[ei]:
                si = mid+1
            else:
                ei = mid-1

    return -1



# Input:
nums = [4,5,6,7,0,1,2]
target = 0
# Output: 4

print(rotated_search(nums,target))
