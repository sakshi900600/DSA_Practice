class Solution:
    def isCycle(self, V, edges):
        #Code here
        # create adjlist
        adjlist = [[] for _ in range(V)]
        
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adjlist[node1].append(node2)
            adjlist[node2].append(node1)
        
        visited = [0]*V
        
        for i in range(V):
            if visited[i] == 0:
                if self.dfs(i,-1,adjlist,visited):
                    return True
        
        return False
        
    
    def dfs(self, src, parent, adjlist, visited):
        visited[src] = 1
        
        for x in adjlist[src]:
            if visited[x] == 0:
                if self.dfs(x,src,adjlist,visited):
                    return True
            elif x != parent:
                return True
        
        return False


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 0)]
    V = 3

    sol = Solution()
    has_cycle = sol.isCycle(V, edges)
    print("Graph contains cycle:" , has_cycle)

    # Output: Graph contains cycle: True