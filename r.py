
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


print(lps("aa"))
