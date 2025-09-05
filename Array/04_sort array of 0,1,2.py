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


def sortArr_count(a):
    c0 = 0
    c1 = 0
    c2 = 0

    n = len(a)

    for it in a:
        if it == 0:
            c0 += 1
        if it == 1:
            c1 += 1
        if it == 2:
            c2 += 1

    
    a[0:c0] = [0]*c0
    a[c0:c0+c1] = [1]*c1
    a[c0+c1:n] = [2]*c2

    return a


# input:
a = [0, 1, 2, 0, 1, 2]
# output:
# a = [0,0,1,1,2,2]

# print(sortarr(a))
print(sortArr_count(a))


# NOTE: the above solution is correct but on gfg you don't need to return array at end.