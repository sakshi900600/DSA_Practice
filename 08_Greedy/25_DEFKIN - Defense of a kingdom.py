def defkin(w,h,n,towers):

    X = list()
    Y = list()

    X.append(0)
    X.append(w+1)
    Y.append(0)
    Y.append(h+1)

    for cord in towers:
        tx , ty = cord
        X.append(tx)
        Y.append(ty)
    
    X.sort()
    Y.sort()

    maxWidth = 0
    for i in range(1, len(X)-1):
        gap = X[i] - X[i-1] - 1
        if gap > maxWidth:
            maxWidth = gap

    maxHeight = 0
    for i in range(1, len(Y)-1):
        gap = Y[i] - Y[i-1] - 1
        if gap > maxHeight:
            maxHeight = gap

    return maxWidth * maxHeight



if __name__ == "__main__":
    w = 15
    h = 8
    n = 3
    towers = [(3, 8), (11, 2), (8, 6)]

    print(defkin(w, h, n, towers))  # Output: 12