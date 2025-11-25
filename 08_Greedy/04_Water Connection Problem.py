#User function Template for python3
class Solution:
    def solve(self, n, p ,a, b, d): 
        #code here
        
        outgoing = [-1]* (n+1)
        incoming = [-1]* (n+1)
        diameter = [float('inf')]* (n+1)
        
        for i in range(p):
            outgoing[a[i]] = b[i]
            incoming[b[i]] = a[i]
            diameter[a[i]] = d[i]
            
        
        ans = []
        
        for i in range(1, n+1):
            # house with no incoming and outgoing will get tank
            if incoming[i] == -1 and outgoing[i] != -1:
                curr = i
                min_dim = float('inf')
                
                while outgoing[curr] != -1:
                    min_dim = min(min_dim, diameter[curr])
                    curr = outgoing[curr]
                
                ans.append([i, curr, min_dim])
        
        
        return ans
                
                




if __name__ == "__main__":
    
    n, p = 9, 6
    a = [7, 5, 4, 2, 9, 3]
    b = [4, 9, 6, 8, 7, 1]
    d = [98, 72, 10, 22, 17, 66]


    # Output: [[2, 8, 22], [3, 1, 66], [5, 6, 10]]
    sol = Solution()
    print(sol.solve(n,p,a,b,d))