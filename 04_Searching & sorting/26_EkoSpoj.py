
# maximum possible height to get at least m amount of wood.
def eko(height,m):
    si = 0
    ei = max(height)
    ans = -1

    while si <= ei:
        mid = (si+ei)//2
        wood = getwood(height, mid)

        if wood >= m:
            ans = mid
            si = mid+1
        else:
            ei = mid-1

    return ans



def getwood(height, wood):
    wood_cnt = 0

    for elem in height:
        if elem > wood:
            wood_cnt += elem - wood

    return wood_cnt



# input: 
height = [20, 15, 10, 17]
m = 7
# Output: 15

height = [4, 42, 40, 26, 46]
m = 20
# Output: 36
print(eko(height, m))

