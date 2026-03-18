from typing import List

class Solution:
    def maximumDistance(self, v: int, e: int, src: int, edges: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(v)]

        for u, v2, w in edges:
            adj[u].append((v2, w))

        vis = [0] * v
        st = []

        # Topological sort
        for i in range(v):
            if vis[i] == 0:
                self.topoDfs(i, vis, adj, st)

        dist = [float('-inf')] * v
        dist[src] = 0

        # Relax edges in topo order
        while st:
            node = st.pop()

            if dist[node] != float('-inf'):
                for neigh, wt in adj[node]:
                    if dist[node] + wt > dist[neigh]:
                        dist[neigh] = dist[node] + wt


        # Convert unreachable nodes to INT_MIN
        INT_MIN = -2**31

        for i in range(len(dist)):
            if dist[i] == float('-inf'):
                dist[i] = INT_MIN

        return dist
        

    def topoDfs(self, node, vis, adj, st):

        vis[node] = 1

        for neigh, wt in adj[node]:
            if vis[neigh] == 0:
                self.topoDfs(neigh, vis, adj, st)

        st.append(node)
        
        
        