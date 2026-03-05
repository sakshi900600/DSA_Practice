#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        n = len(s)
        used = [False]*n
        st = set()
        
        self.generatePerm(0,used,[],s,st)
        
        
        return list(st)
    
    
    def generatePerm(self, idx,used,curr,s,st):
        n = len(s)
        
        if idx == n:
            st.add("".join(curr))
            return
        
        for i in range(n):
            if used[i] == False:
                used[i] = True
                curr.append(s[i])
                self.generatePerm(idx+1, used, curr, s, st)
                curr.pop()
                used[i] = False

    
    # 2nd approach:
    def findPermutation2(self, s):
        # Code here
        n = len(s)
        res = []
        dct = {}
        
        for ch in s:
            dct[ch] = dct.get(ch,0)+1
        
        self.generatePerm2("", dct,res,s)
        
        return res
    
    
    def generatePerm2(self, curr,dct,res,s):
        n = len(s)
        if len(curr) == n:
            res.append(curr)
            return
        
        
        for ch, count in dct.items():
            if count == 0:
                continue
            
            dct[ch] -= 1
            self.generatePerm2(curr+ch, dct,res,s)
            dct[ch] += 1
        
        

if __name__ == "__main__":
    sol = Solution()
    s = "ABC"
    print(sol.findPermutation(s))
    print(sol.findPermutation2(s))

    # Output:
    # ['CAB', 'BAC', 'ACB', 'BCA', 'CBA', 'ABC']
    # ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    