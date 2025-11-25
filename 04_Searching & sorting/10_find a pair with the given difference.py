
# tle - 1110 / 1115 
def findPair(arr,x):
    n = len(arr)
        
    for i in range(n):
        for j in range(i+1,n):
            if abs(arr[i] - arr[j]) == x:
                return True
                    
        
    return False


# using dict
def find_pair_diff(arr,x):

    dct = {}

    for num in arr:
        if num-x in dct or num+x in dct:
            return True
        dct[num] = True

    return False



# input; 
arr = [1,2,3,4,5,6,7,8,9,10]
x = 0

# output: False

print(findPair(arr,x))
print(find_pair_diff(arr,x))