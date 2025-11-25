# this approach gives tle 1110/1111 🤪
def findUnion1(a,b):
    s = set(a)

    union = list(s)

    for i in b:
        if i not in union:
            union.append(i)
    
    return union

    

# all good - ✅
def findUnion2(a,b):
    s1 = set(a)
    s2 = set(b)
    # print(s1)
    # print(s2)

    ans = list(s1.union(s2))
    # print(ans)

    return ans




def findInterset(a,b):
    s1 = set(a)
    s2 = set(b)

    ans = list(s1.intersection(s2))
    
    return ans


# use it ✅
def intersection(a,b):
    n = len(a)
    m = len(b)

    i = 0
    j = 0
    ans = []

    while i<n and j<m:
        if a[i] == b[j]:
            ans.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1


    return ans



# input:
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
# output:
# [1, 2, 3]
# [2, 3]


# input:
# a = [2,8,1]
# b = [9,9,9]
# output:
# [8, 1, 2, 9]
# []


# print(findUnion1(a,b))
# print(findUnion2(a,b)) 

# print(findInterset(a,b))
print(intersection(a,b))
