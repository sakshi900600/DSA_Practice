class Solution:
    def search(self, pat, txt):
        # code here
        n = len(txt)
        m = len(pat)
        
        if m > n:
            return []

        base = 256
        mod = 101
        
        h = 1
        pat_hash = 0
        wndo_hash = 0
        
        ans = []
        
        # here we didn't use pow(base, m-1) because it can be very large and can cause overflow, so we calculate it iteratively and take mod at each step to keep it manageable.

        # highest power h = base^(m-1)
        for i in range(m-1):
            h = (h*base) % mod
        
        
        # initial hash values
        for i in range(m):
            pat_hash = (base * pat_hash + ord(pat[i])) % mod
            wndo_hash = (base * wndo_hash + ord(txt[i])) % mod
            
        
        for i in range(n-m+1):
            if pat_hash == wndo_hash:
                if pat == txt[i:i+m]:
                    ans.append(i)
            
            if i < n-m:
                wndo_hash = (((wndo_hash - ord(txt[i])*h) * base) + ord(txt[i+m])) % mod
                
                if wndo_hash < 0:
                    wndo_hash += mod
        
        
        return ans
                
                
        
# Time Complexity: O(n+m) in average case, O(n*m) in worst case (when there are many hash collisions).


# I didn't understand the initial has value calculation ? What i dry run on paper was simply taking ascii value of each char and multiplying with base m-1 then for next char m-2 and so on....

# --> The formula used for getting initial has values:  
# It builds a polynomial rolling hash efficiently without computing powers separately so both are same. 

# Pattern = "ABC"
# ASCII:
# A = 65
# B = 66
# C = 67

# dry run method result: = 65 * 256^2 + 66 * 256^1 + 67 * 256^0

# Code method (step-by-step) ::::::::--------------------::::::::
# Start:  pat_hash = 0
# Step 1: pat_hash = 256*0 + 65 = 65
# Step 2: pat_hash = 256*65 + 66
# Step 3: pat_hash = 256*(256*65 + 66) + 67
# 👉 Expand it: 65*256^2 + 66*256^1 + 67

# 🔥 SAME as your formula!



# Also why wndo_hash value will be negative and why after adding mod it will be right ?

# ---> wndo_hash can become negative due to subtracting but we want to keep value from 0 to mod-1 (101) without changing its modular value.

        
        
if __name__ == "__main__":

    sol = Solution()

    txt = "abcab"
    pat = "ab"
    # Output: [0, 3]

    print(sol.search(pat,txt))

