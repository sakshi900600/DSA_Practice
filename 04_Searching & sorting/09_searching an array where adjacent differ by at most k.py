def searchx(arr, k,x):
    n = len(arr)
    i = 0
    while i<n:
        if arr[i] == x:
            return i
        i = i + max(1, abs(arr[i]-x)//k)
    
    return -1


# input:
a = [20,40,50,70,70,60]
k = 20
x = 60

# output: 5

print(searchx(a,k,x))