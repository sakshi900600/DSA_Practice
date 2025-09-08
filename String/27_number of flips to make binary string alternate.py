

# see there can be only 2 possiblities . either string starts with 0 or 1. 
# if start with 0 then it will go like this:  010101...
# if start with 1 then it will go like this; 101010...

# if we check only for one patter then it will give total but we need minimum . so we will apply both patterns and get minimum of it. Got it 👍

def min_flips(s):
    n = len(s)

    flip0 = 0
    flip1 = 0

    for i in range(n):
        # starts with 0
        if i%2==0:
            if s[i] == '0':
                flip1 += 1
            else:
                flip0 += 1
        else:
            if s[i] == '1':
                flip1 += 1
            else:
                flip0 += 1



    ans = min(flip0,flip1)

    # print(ans)
    return ans
            


# input:
s = "001"

# output: 1
print(min_flips(s))
