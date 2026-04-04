def get_badchar(pat):
    m = len(pat)

    badchar = [-1]*256

    for i in range(m):
        badchar[ord(pat[i])] = i
    
    return badchar


def boyer_moore(pat, txt):
    n = len(txt)
    m = len(pat)

    badchar = get_badchar(pat)

    shift = 0
    ans = []

    while shift <= n-m:
        j = m-1

        while j>=0 and pat[j]==txt[shift+j]:
            j -= 1
        
        # if found
        if j < 0:
            ans.append(shift)
            # shift for other solution
            if shift+m < n:
                shift += (m-badchar[ord(txt[shift+m])])
            else:
                shift += 1
        
        else:
            shift += max(1, j-badchar[ord(txt[shift+j])])


    return ans




txt = "AABAACAADAABAABA"
pat = "AABA"
print(boyer_moore(pat,txt))

# Output: [0,9,12]
