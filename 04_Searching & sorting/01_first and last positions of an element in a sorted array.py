
def first_occurence(arr,si,ei,x):

    # first occurence
    first = -1
    while si <= ei:
        mid = (si+ei)//2

        if arr[mid] == x:
            first = mid
            ei = mid-1
        elif arr[mid] > x:
            ei = mid-1
        else:
            si = mid+1

    
    return first


def last_occurence(arr,si,ei,x):

    # first occurence
    last = -1
    while si <= ei:
        mid = (si+ei)//2

        if arr[mid] == x:
            last = mid
            si = mid+1
        elif arr[mid] < x:
            si = mid+1
        else:
            ei = mid-1

    
    return last




arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5


# arr = [1, 3, 5, 5, 5, 5, 7, 123, 125]
# x = 7


# arr = [1,2,3]
# x = 4


n = len(arr)
print(first_occurence(arr,0,n-1,x))
print(last_occurence(arr,0,n-1,x))