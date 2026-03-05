
# recursive approach:
def getsubseq(s,idx,subsequence):
    if idx == len(s):
        print(subsequence,end=" ")
        return 
    
    # take
    getsubseq(s,idx+1, subsequence+s[idx])
    getsubseq(s,idx+1,subsequence)



# bit manipulation approach: 
def getSubseq(s, num):
    j = 0
    subseq = ""

    while num > 0:
        # check all the set bit and add those index char in our subseq string
        if (num & 1):
            subseq += s[j]
        j += 1

        # right shift digit by 1 to check next bit
        # num = num // 10 - you can't do this coz here num represents binary number, not decimal so we have to right shift it by 1
        num = num >> 1
    
    return subseq


def allSubseq(s):
    n = len(s)
    ans = []

    # for a string of n length total subsequence will be 2^n

    # for i in range(2**n): or we can write it as 1<<n
    for i in range(1<< n):
        ans.append(getSubseq(s,i))

    return ans




# input
s = "abc"

subsequence = ""
getsubseq(s,0,subsequence)

print(allSubseq(s))

# output
# abc ab ac a bc b c  
# ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
