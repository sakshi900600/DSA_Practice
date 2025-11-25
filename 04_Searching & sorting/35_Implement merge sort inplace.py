
def merge_sort(a,si,ei):

    if si >= ei:
        return
    
    mid = (si+ei)//2
    merge_sort(a,si,mid)
    merge_sort(a,mid+1,ei)

    merge(a,si,mid,ei)


def merge(a,si,mid,ei):
    i = si
    j = mid+1

    while i<=mid and j<=ei:
        if a[i] <= a[j]:
            i += 1
        else:
            # rotate arr value from i to j
            value = a[j]
            idx = j

            while idx != i:
                a[idx] = a[idx-1]
                idx -= 1
            
            a[i] = value

            i += 1
            mid += 1 # coz second arrays one elem comes in 1st array so mid will increase by 1. 
            j += 1



# input:
a = [2, 3, 4, 1,5]
n = len(a)
merge_sort(a,0,n-1)
print(a)


