
def get_square_root(n):
        
    si = 0
    ei = 1001
    ans = 0

    while si <= ei:
        mid = (si+ei)//2
            
        if mid * mid == n:
            ans = mid
            break
        elif mid * mid < n:
            ans = mid
            si = mid+1
        else:
            ei = mid-1
                
    return ans



# count squares less than n:
def count_square(n):
    count = 0

    rootn = int(math.sqrt(n))

    for i in range(1,rootn+1):
        if i*i < n:
            count += 1
    
    return count


import math

# print(math.sqrt(16)) # float value
# print(math.isqrt(16)) # int value
# print(get_square_root(98))



# input:
n = 9
# output:
# 2


print(count_square(n))
