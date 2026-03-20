# User function Template for python3

class Solution:
    def mColoring(self, v, edges, m):
        # code here
        adj = [[] for _ in range(v)]
        for x  in edges:
            node1 = x[0]
            node2 = x[1]
            
            adj[node1].append(node2)
            adj[node2].append(node1)
            
        colors = [-1]*v
        
        
        def helper(cnode):
            if cnode == v:
                return True
            
            for i in range(m):
                if self.isSafe(cnode,i,colors,adj):
                    colors[cnode] = i
                    if helper(cnode+1):
                        return True
                    colors[cnode] = -1
            
            return False
        
        return helper(0)
        
    
    def isSafe(self, node, ncol, colors,adj):
        
        for neigh in adj[node]:
            if colors[neigh] == ncol:
                return False
            
        return True
        
        

if __name__ == "__main__":
    sol = Solution()

    v = 4
    edges = [[0, 1], [0, 2], [1, 2], [1, 3]]
    m = 3

    print(sol.mColoring(v, edges, m))  
    # Output: True

    