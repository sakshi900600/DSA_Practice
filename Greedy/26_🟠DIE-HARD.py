
# not fully clear ->>>>>>>>>>

def die_hard(h,a):
    memo = {}
    # zone = 0:Air, 1:Water, 2:Fire
    def helper(hp, ar, zone):
        if hp <=0 or ar<=0:
            return 0
        
        if (hp,ar,zone) in memo:
            return memo[(hp, ar, zone)]
        
        # go into one zone and update the value and call for rest 2 options and get max of both

        if zone == 0: # air
            hp1 = hp + 3
            ar1 = ar + 2
            # options: water and fire

            o1 = 1 + helper(hp1-5, ar1-10, 1)
            o2 = 1 + helper(hp1-20, ar1+5, 2)

            memo[(hp, ar, 0)] = max(o1, o2)
        elif zone == 1: # water
            hp1 = hp - 5
            ar1 = ar - 10
            # options: air and fire

            o1 = 1 + helper(hp1+3, ar1+2, 0)
            o2 = 1 + helper(hp1-20, ar1+5, 2)

            memo[(hp, ar, 1)] = max(o1, o2)
        else: # fire
            hp1 = hp - 20
            ar1 = ar + 5
            # options: air and water

            o1 = 1 + helper(hp1+3, ar1+2, 0)
            o2 = 1 + helper(hp1-5, ar1-10, 1)

            memo[(hp, ar, 2)] = max(o1, o2)
        
        return memo[(hp, ar, zone)]
    
    return helper(h, a, 0)


if __name__ == '__main__':

    h = 20
    a = 8
    # Output: 5
    print(die_hard(h,a)) # wrong ❌

