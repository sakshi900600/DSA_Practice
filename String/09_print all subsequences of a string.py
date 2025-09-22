def subseq(s,idx,subsequence):
    if idx == len(s):
        print(subsequence,end=" ")
        return 
    
    # take
    subseq(s,idx+1, subsequence+s[idx])
    subseq(s,idx+1,subsequence)



# input
s = "aab"

# output
# ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']


subsequence = ""
subseq(s,0,subsequence)



def subseq_opt():
    s = "abc"
    n = len(s)
    ans = []

    for i in range(1<<n):
        subseq = ""

        for j in range(n):
            if i & 1<<j:
                subseq += s[j]

        ans.append(subseq)


    print(ans)



subseq_opt()