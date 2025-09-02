def subseq(s,idx,subsequence):
    if idx == len(s):
        print(subsequence,end=" ")
        return 
    
    # take
    subseq(s,idx+1, subsequence+s[idx])
    subseq(s,idx+1,subsequence)


s = "ab"
subsequence = ""
subseq(s,0,subsequence)

