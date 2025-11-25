def romanToDecimal(s):

    decimal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    n = len(s)
    ans = 0
    for i in range(n-1):
        if decimal[s[i]] < decimal[s[i+1]]:
            ans -= decimal[s[i]]
        else:
            ans += decimal[s[i]]

    # for last char 
    ans += decimal[s[-1]]

    return ans



s = "MCMIV"
# Output: 1904

print(romanToDecimal(s))
