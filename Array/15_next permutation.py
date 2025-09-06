def decimal_binary(num):
    binary = ""
    if num == 0:
        return 0
    
    while num > 0:
        rem = num % 2
        binary += str(rem)
        num = num//2

    return binary[::-1]



# print(decimal_binary(15))



# given a number return all the binary string of that size. 

# generate total binary string of n size. total possiblities = 2^n

# print(decimal_binary(1))

n = 5
ans = []
k = 2**n  # ** - power oprator -> pow()


for i in range(k):
    s = str(decimal_binary(i)) 

    # add 0 in starting to make it n lenght
    if len(s) < n:
        s = (n-len(s))* '0' + s
    ans.append(s)

print(ans)




class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i = n-2

        while i>=0 and nums[i+1] <= nums[i]:
            i -= 1

        
        if i>=0:
            j = n-1

            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i],nums[j] = nums[j],nums[i]

        
        start = i+1
        end = n-1

        while start < end:
            nums[start],nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return nums



        
if __name__ == "__main__":
    sol = Solution()

    nums = [1,2,3]
    nums = [1,3,2]
    print(sol.nextPermutation(nums))






