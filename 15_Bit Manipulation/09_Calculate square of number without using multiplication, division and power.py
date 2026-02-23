def square(n):
    if n < 0:
        n = -n

    res = n
    for i in range(1,n):
        res += n
    
    return res


def square_opt(num):
    if num < 0:
        num = -num
    
    power,result = 0,0
    temp = num

    while temp:
        if temp & 1: #odd
            # result = result + (num*(2^power))
            result += (num << power)
        power += 1
    
        # temp = temp // 2
        temp = temp >> 1
    
    return result



n = 5
print(square(5)) # 25
print(square_opt(7)) # 49
