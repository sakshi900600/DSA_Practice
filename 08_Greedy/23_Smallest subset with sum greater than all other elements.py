# User function Template for python3

class Solution:
    # works but tle: 
    def minSubset(self, arr):
        # code here
        
        arr.sort(reverse="True")
        total_sum = sum(arr)
        min_len = float('inf')
        
        
        i = 0
        for j in range(len(arr)):
            subset = arr[i:j+1]
            subset_sum = sum(subset)
            
            if subset_sum > total_sum-subset_sum:
                min_len = min(min_len, j-i+1)
                break
        
        return min_len


    def minSubset_opt(self, arr):
        # code here
        
        arr.sort(reverse="True")
        total_sum = sum(arr)
        
        length = 0
        curr_sum = 0
        for j in range(len(arr)):
            curr_sum += arr[j]
            length += 1
            
            if curr_sum > total_sum - curr_sum:
                break
        
        
        return length
    


if __name__ == '__main__':
    sol = Solution()

    # input:
    arr = [2,17,7,3]

    # Output: 1
    print(sol.minSubset(arr))  
    print(sol.minSubset_opt(arr))  