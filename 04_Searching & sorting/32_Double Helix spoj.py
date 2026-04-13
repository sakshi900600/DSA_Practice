
def doubleHelix(l1, l2):
    i = 0
    j = 0

    n = len(l1)
    m = len(l2)

    sum1 = 0
    sum2 = 0
    maxSum = 0

    while i < n and j < m:
        if l1[i] < l2[j]:
            sum1 += l1[i]
            i += 1
        elif l1[i] > l2[j]:
            sum2 += l2[j]
            j += 1
        else:
            cmax = max(sum1, sum2)
            maxSum += cmax
            maxSum += l1[i]
            i += 1
            j += 1

            sum1, sum2 = 0, 0
    
    while i < n:
        sum1 += l1[i]
        i += 1
    while j < m:
        sum2 += l2[j]
        j += 1
    
    maxSum += max(sum1, sum2)

    return maxSum




# input
l1 = [3,5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62]
l2 = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]
# Output: 450
print(doubleHelix(l1, l2))


l1 = [-5,100,1000,1005]
l2 = [-12,1000,1001]
# Output: 2100
print(doubleHelix(l1,l2))
