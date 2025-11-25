def findk_max_min(a,k):
    a = sorted(a)
    n = len(a)

    mini = a[k-1]
    maxi = a[n-k]

    return [mini,maxi]



# without using inbuilt function
def findk_min(a,k):
    
    mini = a[0]
    for _ in range(k):
        mini = min(a)
        a.remove(mini)
    
    return mini
    
def findk_max(a,k):
    
    maxi = a[0]
    for _ in range(k):
        maxi = max(a)
        a.remove(maxi)
    
    return maxi
    



# input:
a = [7, 10, 4, 3, 20, 15]
k = 2
# output:
# [7, 10]

# print(findk_max_min(a,k))

print(findk_min(a,k))
print(findk_max(a,k))



        