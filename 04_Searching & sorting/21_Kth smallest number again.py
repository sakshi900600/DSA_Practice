# find kth smallest no in the given range.
# ex- (1,5)(3,7)(10,15) , k = 9
# if we write it as arr : 1,2,3,4,5,6,7,10,11,12,13,14,15
# so 9th smallest no is: 11

# To solve it: 
# 2. sort ranges
# 1. merge the ranges
# 3. find kth smallest

# how to get kth smallest:
# check if k comes in the first range diff(include last number of range as well) : if yes then ans will be (start num of range + k -1)
# else: update k as (k-range diff) & search in another range 


def merge_intervals(intervals):
    n = len(intervals)
    intervals.sort()

    idx = 0
    for i in range(1,n):
        curr = intervals[i]
        last = intervals[idx]
        if last[1] >= curr[0]:
            last[1] = max(curr[1],last[1])
        else:
            idx += 1
            intervals[idx] = curr

    return intervals[:idx+1] 


def kth_smallest(ranges, k):
    sorted_ranges = merge_intervals(ranges)

    for r in sorted_ranges:
        diff = r[1] - r[0] + 1
        if k <= diff:
            return r[0]+k-1
        else:
            k -= diff

    return -1


# input
ranges = [[1, 5], [3, 7], [10, 15]]
k = 9
# Output: 11

print(kth_smallest(ranges, k))
