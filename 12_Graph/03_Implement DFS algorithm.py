class Solution:
    def dfs(self, adj):
        # code here
        n = len(adj)
        visited = [0]*n
        li = []
        
        for i in range(n):
            if visited[i] == 0:
                self.dfs_helper(i, adj,visited,li)
                
        return li
        
        
    
    def dfs_helper(self, node, adj, visited, li):
        visited[node]= 1
        li.append(node)
        
        for adjnode in adj[node]:
            if visited[adjnode] == 0:
                self.dfs_helper(adjnode, adj, visited, li)
                


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    V = 7

    # Create adjacency list
    adjlist = [[] for _ in range(V)]
    for x in edges:
        node1 = x[0]
        node2 = x[1]
        adjlist[node1].append(node2)
        adjlist[node2].append(node1)

    solution = Solution()
    result = solution.dfs(adjlist)
    print("DFS Traversal:", result)

    # Output: DFS Traversal: [0, 1, 3, 4, 2, 5, 6]