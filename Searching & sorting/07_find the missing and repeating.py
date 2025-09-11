
# Approach:
# 1. i tried brute force which is using loops: but that give tle.

# 2. using math equations: 
# s1: basically lets say repeating and missing = r,m

# s2: find expected sum(1-n), given arr sum  and expected square sum(1-n), given arr square sum

# s3: then take difference: 
# ΔS = actualSum - expectedSum = r-m   --------------- eq1
# ΔQ = actualSqSum - expectedSqSum = r^2 - m^2  ------------ eq2

# now a2-b2 = (a+b)(a-b) put in eq2 and put value from eq1 and simplfify it
# here r+m(sumRM) = ΔQ / ΔS  ----------  eq2

# after adding both equation :
# R = (ΔS + sumRM)/2
# M = R - ΔS

# and that's our answer. 





def missing_repeating(arr):

    n = len(arr)

    expected_sum = (n * (n+1))//2
    arr_sum = sum(arr)

    # sum difference:
    ds = arr_sum - expected_sum


    expected_sq_sum = (n*(n+1)*(2*n+1))//6
    arr_sq_sum = 0

    for i in arr:
        arr_sq_sum += i*i
    

    # square sum difference:
    dq = arr_sq_sum - expected_sq_sum


    # r+m = square sum difference /sum difference
    sumRM = dq//ds

    # repeating no = R, missing = M
    R = (ds+sumRM)//2

    M = R - ds


    return [R,M]
    
    



arr = [4,3,6,2,1,1]
print(missing_repeating(arr))