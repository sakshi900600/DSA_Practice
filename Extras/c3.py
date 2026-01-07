# 1. reverse string prefix
def reverse_prefix(s, k):

    if k == 1:
        return s

    part1 = s[:k]
    part2 = s[k:]

    rev_part1 = part1[::-1]
    ans = rev_part1 + part2

    return ans


# 2. minimum subarray length with distinct sum at least k
def minLength(nums, k):
    n = len(nums)

    minlen = float('inf')

    for i in range(n):
        sum = nums[i]
        if sum >= k:
            return 1

        count = 1
        for j in range(i+1,n):
            
            if nums[j] != nums[i]:
                sum += nums[j]
                count += 1

                if sum >= k:
                    minlen = min(minlen, count)
                    break
    
    if minlen == float('-inf'):
        return -1
    
    return minlen



if __name__ == "__main__":

    # s = "hey"
    # k = 1

    # s = "xyz"
    # k = 3

    # s = "abcd"
    # k = 2
    # print(reverse_prefix(s,k))


    # 2 -----------------------------
    nums = [2,2,3,1]
    k = 4

    # nums = [3,2,3,4]
    # k = 5

    # nums = [5,5,4]
    # k = 5

    # nums = [1,12]
    # k = 7
    print(minLength(nums,k))