
def minMoves(nums):
    n = len(nums)
    nums.sort()
    moves = 0
    larg_num = nums[-1]
    for i in range(n):
        moves += larg_num - nums[i]

    return moves


def countMajoritySubarrays(nums,target):
    n = len(nums)

    # count = 0
    # for i in range(n):
    #     for j in range(i,n):
    #         subarr = nums[i: j+1]
    #         melem = get_majority(subarr)

    #         if melem == target:
    #             count += 1
    
    # return count

    # how to optimize this?
    count = 0
    for i in range(n):
        freq = {}
        for j in range(i,n):
            num = nums[j]
            freq[num] = freq.get(num,0) + 1
            length = j - i + 1
            if freq[num] > length // 2:
                melem = num
            else:
                melem = -1

            if melem == target:
                count += 1

    return count





def get_majority(arr):
    freq = {}
    n = len(arr)
    for num in arr:
        freq[num] = freq.get(num,0) + 1

    for key in freq:
        if freq[key] > n//2:
            return key
    return -1




class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        count = 0
        
        for i in range(n):
            freq = {}
            for j in range(i, n):
                # Update frequency of current element
                num = nums[j]
                freq[num] = freq.get(num, 0) + 1
                length = j - i + 1
                
                # Check if target is majority element
                if freq.get(target, 0) > length // 2:
                    count += 1
                    
        return count




# a = [2,1,3]
# # a  = [4,4,5]
# print(minMoves(a))


# nums = [1,2,2,3]
nums = [1,1,1,1]
nums = [1,2,3]
target = 4

# print(countMajoritySubarrays(nums,target))

sol = Solution()
print(sol.countMajoritySubarrays(nums,target))