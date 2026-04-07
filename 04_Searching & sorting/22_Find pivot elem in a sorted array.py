# pivot elem: elem from where the array is rotated.

def findPivot(arr):
    n = len(arr)

    si = 0
    ei = n-1

    while si < ei:
        mid = (si+ei)//2

        if arr[mid] > arr[ei]:
            si = mid+1
        else:
            ei = mid
    
    return si



arr = [4,5,6,7,1,2,3]
print(findPivot(arr))
