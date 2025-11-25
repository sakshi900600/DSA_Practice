def longestConsecutive(a):
    s = set(a)
    longest = 0

    for x in s:
        if x-1 not in s:
            y = x
            while y+1 in s:
                y = y+1
            longest = max(longest, y-x+1)
    
    return longest



class Solution:
    
    def longestConsecutive(self, a):
        if not a:  # Handle empty array
            return 0
            
        a.sort()
        
        max_count = 1
        count = 1
        
        for i in range(len(a)-1):
            if a[i+1] - a[i] == 1:
                count += 1
            elif a[i+1] == a[i]:  # Skip duplicates
                continue
            else:
                max_count = max(max_count, count)
                count = 1
        
        # Final check after loop ends
        max_count = max(max_count, count)
        
        return max_count





# Input:
arr = [2, 6, 1, 9, 4, 5, 3]
# Output: 6

sol = Solution()

print(longestConsecutive(arr))
print(sol.longestConsecutive(arr))