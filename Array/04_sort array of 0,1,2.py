def sortarr(a):
    left = 0
    mid = 0
    right = len(a)-1

    while mid <= right:
        if a[mid] == 0:
            temp = a[left]
            a[left] = a[mid]
            a[mid] = temp
            left += 1
            mid += 1
        
        elif a[mid] == 1:
            mid += 1
        
        else:
            temp = a[right]
            a[right] = a[mid]
            a[mid] = temp
            right -= 1

    return a




# input:
a = [0, 1, 2, 0, 1, 2]
# output:
# a = [0,0,1,1,2,2]

print(sortarr(a))


# NOTE: the above solution is correct but on gfg you don't need to return array at end.