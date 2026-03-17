# method-1: m-colouring problem
class Solution1:
    def graphColoring(self, v, edges, m):
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
        

# method-2: BFS
from collections import deque
class Solution2:
    def isBipartite(self, V, edges):
        # code here
        adj = [[] for _ in range(V)]
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adj[node1].append(node2)
            adj[node2].append(node1)
            
        colors = [-1]*V
        return self.bfs(V,adj,colors)
        
    
    def bfs(self, V,adj,colors):
        q = deque()
        q.append(0)
        colors[0] = 0
        
        while q:
            node = q.popleft()
            
            for neigh in adj[node]:
                if colors[neigh] == -1:
                    colors[neigh] = 1- colors[node]
                    q.append(neigh)
                elif colors[neigh] == colors[node]:
                    return False
        
        return True
        

# method-3: DFS
class Solution3:
    def isBipartite(self, V, edges):
        # code here
        adj = [[] for _ in range(V)]
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adj[node1].append(node2)
            adj[node2].append(node1)
            
        colors = [-1]*V
        return self.dfs(0,0,V,adj,colors)
        
    
    def dfs(self,node,ncol, V,adj,colors):
        colors[node] = ncol
            
        for neigh in adj[node]:
            if colors[neigh] == -1:
                if not self.dfs(neigh,1-ncol,V,adj,colors):
                    return False
                   
            elif colors[neigh] == colors[node]:
                return False
        
        return True
        
                    
             

if __name__ == "__main__":

    v = 4
    edges = [[0, 1], [0, 2], [1, 2], [1, 3]]
    m = 2 # always 2 for bipartite graph

    # Using m-colouring method
    sol1 = Solution1()
    print(sol1.graphColoring(v, edges, m))  
    # Output: False

    # Using BFS method
    sol2 = Solution2()
    print(sol2.isBipartite(v, edges))
    # Output: False

    # Using DFS method
    sol3 = Solution3()
    print(sol3.isBipartite(v, edges))
    # Output: False
    
    