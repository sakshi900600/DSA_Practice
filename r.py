
# maxm profit by buy & sell stock at most twice
# median of 2 sorted array

# def fun(a):
    
    




# arr = [1, 4, 45, 6, 0, 19]
# print(fun(arr))

# arr.sort(key)



# finding lps
def lps(s):
    longest = float("-inf")
    n = len(s)

    if n == 1:
        return 0

    for i in range(1,n-1):
        prefix = s[:i]
        suffix = s[i+1:]

        if prefix == suffix:
            longest = max(longest, len(prefix))
        
    return longest


# print(lps("aa"))








# find pair with given diff
# find 4 elem that sums to given val
# maxm sum such that no 2 elem are adj
# count triplet sum smaller that a given val
# merge 2 sorted arrays
# print all subarr with 0 sum
# product arr puzzle
# sort arr acc to count of set bit


def f(arr):
    n = len(arr)
    x = 45
    dct = {}

    for i in arr:
        if i-x in dct or i+x in dct:
            return True
        dct[i] = 1
    
    return False
    




arr = [90, 70, 20, 80, 50]
print(f(arr))