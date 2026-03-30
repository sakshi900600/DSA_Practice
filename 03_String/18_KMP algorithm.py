#Function to check if the pattern exists in the string or not.
def KMP(pat, txt):
    #code here
    m = len(pat)
    n = len(txt)
    
    # Handle edge cases
    if m == 0:
        return True  # Empty pattern is considered present
    if n == 0 or m > n:
        return False
    
    lps = [0]*m
    computeLPSArray(pat, m, lps)
    
    i = 0  # index for txt
    j = 0  # index for pat
    ans = []
    
    while i < n:
        # If characters match, move both pointers
        if txt[i] == pat[j]:
            i += 1
            j += 1
        
        # If we found a complete match
        if j == m:
            ans.append(i - j)
            j = lps[j-1]  # Look for the next match
        
        # If characters don't match
        elif i < n and txt[i] != pat[j]:
            if j != 0:
                j = lps[j-1]  # Use LPS to skip comparisons
            else:
                i += 1  # Move to next character in text
    
    # Return True if at least one match found, False otherwise
    return len(ans) > 0



#Function to fill lps[] for given pattern pat[0..M-1].  
def computeLPSArray(pat, M, lps):
    #Your code here
    
    length = 0  # length of the previous longest prefix suffix
    i = 1       # start from index 1
    lps[0] = 0  # lps[0] is always 0
    
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # fall back to previous LPS value
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
                
                
# If ques asks to return lsp for a whole string then return lps[-1] not max(lps).


