def inversion(a):
    return merge_count(a,0,len(a)-1)


def merge_count(a,si,ei):
    if si >= ei:
        return 0

    inversion = 0
    mid = (si+ei)//2

    inversion += merge_count(a,si,mid)
    inversion += merge_count(a,mid+1, ei)
    inversion += merge(a,si,mid,ei)

    return inversion


def merge(a,si,mid,ei):
    i = si
    j = mid+1
    temp = []
    inversion = 0

    while i<=mid and j <= ei:
        if a[i] < a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            inversion += (mid-i+1)
            j += 1
    

    while i <= mid:
        temp.append(a[i])
        i += 1
    
    while j <= ei:
        temp.append(a[j])
        j += 1
    

    # copy
    for k in range(si, ei+1):
        a[k] = temp[k-si]
    

    return inversion



# input
a = [2, 4, 1, 3, 5]

# output: 3

print(inversion(a))

