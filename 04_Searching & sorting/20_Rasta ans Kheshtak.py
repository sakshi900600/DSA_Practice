
# Biggest Common Subsquare
def rasta_kheshtak(A, B):
    n = len(A)
    m = len(A[0])

    max_size = 0

    for i in range(n):
        for j in range(m):
            for x in range(n):
                for y in range(m):
                    # matched - start point
                    if A[i][j] == B[x][y]:
                        size = getsize(A,B,i,j,x,y,n,m)
                        max_size = max(max_size, size)

    return max_size


def getsize(A,B,i,j,x,y,n,m):
    size = 0

    while True:
        # boundary
        if i+size >= n or j+size >=m or x+size>=n or y+size>=m:
            break

        for a in range(size+1):
            for b in range(size+1):
                if A[i+a][j+b] != B[x+a][y+b]:
                    return size
        size += 1

    return size



# Input:
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[0,2,3],[4,5,6],[7,8,0]]
# Output: 2

print(rasta_kheshtak(A,B))