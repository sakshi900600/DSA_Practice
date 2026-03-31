class Solution:
    def generateIp(self, s):
        # Code here
        n = len(s)
        ans = []
        
        def helper(idx, curr):
            if len(curr) == 4:
                if idx == n:
                    ans.append(".".join(curr))
                    return
            
            # valid num will be of either 1,2 or 3 digits,so
            for length in range(1,4):
                if idx+length > n:
                    break
                
                part = s[idx: idx+length] # 1\2\3 digits
                
                # trailing zero
                if len(part)>1 and part[0]=='0':
                    continue
                
                # 0-255 check
                if int(part) > 255:
                    continue
                
                curr.append(part)
                helper(idx+length, curr)
                curr.pop()
                
        
        helper(0,[])
        
        return ans
                
                
                

if __name__ == "__main__":

    sol = Solution()
    s = "255678166"
    print(sol.generateIp(s)) 
    
    # Output: ['25.56.78.166', '255.6.78.166', '255.67.8.166', '255.67.81.66']
    