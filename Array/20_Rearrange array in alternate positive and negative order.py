def rearrange(arr):

    pos = []
    neg = []

    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    

    posIdx = 0
    negIdx = 0
    i = 0

    while posIdx < len(pos) and negIdx < len(neg):
        if i%2 == 0:
            arr[i] = pos[posIdx]
            posIdx += 1
        else:
            arr[i] = neg[negIdx]
            negIdx += 1
        
        i += 1
    
    # rest pos and neg elements
    while posIdx < len(pos):
        arr[i] = pos[posIdx]
        posIdx += 1
        i += 1
    
    while negIdx < len(neg):
        arr[i] = neg[negIdx]
        negIdx += 1
        i += 1


    return arr



# input:
arr = [1, 2, 3, -4, -1, 4]

# Output: arr = [1, -4, 2, -1, 3, 4]

print(rearrange(arr))

    