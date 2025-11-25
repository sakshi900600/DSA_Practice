def get_min_max(arr):

    n = len(arr)
    if n == 0:
        return []
    
    if n == 1:
        return [arr[0],arr[0]]
    

    p = [arr[0], arr[1]] # min,max

    if p[0] > p[1]:
        p[0],p[1] = p[1], p[0]


    # print(p)

    i = 2
    while i < n-1:
        if arr[i] < arr[i+1]:
            cmin = arr[i]
            cmax = arr[i+1]
        else:
            cmin = arr[i+1]
            cmax = arr[i]
        
        p[0] = min(p[0], cmin)
        p[1] = max(p[1], cmax)

        i += 2
    

    if n % 2 != 0:
        last = arr[-1]

        p[0] = min(last,p[0])
        p[1] = max(last,p[1])

    return p



# ques whose link was given - solution:

def middle(a,b,c):

    # middle element :  first way is to compare it with other elements but ques says min no of comparisons:

    # so if you find out total sum = a+b+c and then
    # sub the max and min value then the one value will be left which will be our middle value. 

    return a+b+c - min(a,b,c) - max(a,b,c)





# input:
arr = [3, 2, 1, 56, 10000, 167]

# output:
# [1, 10000]

# print(get_min_max(arr))



# input:
a = 978
b = 518
c = 300
# Output: 518

print(middle(a,b,c))

