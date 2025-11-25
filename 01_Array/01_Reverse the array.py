def reverseArr(a):
    si = 0
    ei = len(a)-1

    while si < ei:
        temp = a[si]
        a[si] = a[ei]
        a[ei] = temp
        si += 1
        ei -=1

    # return a[::-1]
    return a


# input: 
a = [1,2,3,4,5]
# output:
# [5, 4, 3, 2, 1]

print(reverseArr(a))