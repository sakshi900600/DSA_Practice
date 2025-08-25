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



# Input:
arr = [2, 6, 1, 9, 4, 5, 3]
# Output: 6

print(longestConsecutive(arr))