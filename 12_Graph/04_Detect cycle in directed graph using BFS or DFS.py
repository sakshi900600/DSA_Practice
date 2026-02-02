class Solution:
    def isCyclic(self, V, edges):
        # code here
        # create adjlist
        adjlist = [[] for _ in range(V)]
        
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adjlist[node1].append(node2)
        
        
        visited = [0]*V
        curr_path = [0]*V
        
        for i in range(V):
            if visited[i] == 0:
                if self.dfs(i,curr_path,adjlist,visited):
                    return True
        
        return False
        
    
    def dfs(self, src, curr_path, adjlist, visited):
        visited[src] = 1
        curr_path[src] = 1
        
        for x in adjlist[src]:
            if visited[x] == 0:
                if self.dfs(x,curr_path,adjlist,visited):
                    return True
                    
            elif visited[x] == 1 and curr_path[x] == 1:
                return True
        
        
        curr_path[src] = 0
        return False
        


if __name__ == "__main__":
    sol = Solution()

    V = 4
    edges = [[0, 1], [1, 2], [2, 0], [2, 3]]

    print(sol.isCyclic(V,edges))
    # Output: True

    