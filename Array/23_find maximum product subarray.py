
def maxProduct(arr):
    max_product = arr[0]
    cmax = arr[0]
    cmin = arr[0]

    for x in arr[1:]:
        if x < 0:
            cmax,cmin = cmin,cmax
        
        cmax = max(x, x*cmax)
        cmin = min(x, x*cmin)

        max_product = max(max_product, cmax)

    return max_product



# input:
arr = [-2, 6, -3, -10, 0, 2]

# Output: 180

print(maxProduct(arr))
