
from collections import deque
class Solution:
    def bfs(self, adj):
        # code here
        n = len(adj)
        visited = [0]*n
        
        q = deque()
        q.append(0)
        visited[0] = 1
        
        li = []
        
        while q:
            node = q.popleft()
            li.append(node)
            
            for x in adj[node]:
                if visited[x] == 0:
                    visited[x] = 1
                    q.append(x)
        
        return li
                    


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    V = 7

    # Create adjacency list
    def create_graph_list(edges, V):
        adjlist = [[] for _ in range(V)]

        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adjlist[node1].append(node2)
            adjlist[node2].append(node1)

        return adjlist

    adj = create_graph_list(edges, V)

    sol = Solution()
    result = sol.bfs(adj)
    print("BFS Traversal:", result)

    # Output: BFS Traversal: [0, 1, 2, 3, 4, 5, 6]
