def findk_max_min(a,k):
    a = sorted(a)
    n = len(a)

    mini = a[k-1]
    maxi = a[n-k]

    return [mini,maxi]


# input:
a = [7, 10, 4, 3, 20, 15]
k = 3
# output:
# [7, 10]

print(findk_max_min(a,k))