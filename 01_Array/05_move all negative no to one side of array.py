def moveNeg(a):
    left = 0
    n = len(a)

    for right in range(n):
        if a[right] < 0:
            # swapping without 3rd variable
            # a[left],a[right] = a[right],a[left]
            temp = a[left]
            a[left] = a[right]
            a[right] = temp

            left += 1
    
    return a


def moveNegative(a):
    left = 0
    right = len(a)-1

    while left < right:

        while left<right and a[left] < 0:
            left += 1
        
        while left < right and a[right] > 0:
            right -= 1

        if left < right:
            a[left],a[right] = a[right],a[left]
            left += 1
            right -= 1
            
    return a



# input:
a = [-12, 11, -13, -5, 6, -7, 5, -3, -6]


# output:
print(moveNeg(a))
# [-12, -13, -5, -7, -3, -6, 5, 6, 11]


# output:
# print(moveNegative(a))
# [-12, -6, -13, -5, -3, -7, 5, 6, 11]
