def kadaneAlgo(a):
    n = len(a)

    sum = a[0]
    max_sum = a[0]

    for i in range(1,n):
        if sum >= 0:
            sum += a[i]
        else:
            sum = a[i]
        
        if sum > max_sum:
            max_sum = sum
    

    return max_sum



# input:
arr = [2, 3, -8, 7, -1, 2, 3]
# output: 11


print(kadaneAlgo(arr))
