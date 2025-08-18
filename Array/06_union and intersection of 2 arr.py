# this approach takes n^2 tc  coz everytime checking if that elem is in list or not. so can give tle

def findUnion1(a,b):
    union = []

    for i in a:
        if i not in union:
            union.append(i)

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

print(findUnion2(a,b))
print(findInterset(a,b))
