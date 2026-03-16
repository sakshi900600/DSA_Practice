from collections import deque

class Solution:
    def isBridge(self, V, edges, c, d):
        # 1. Build the adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # store all the bridges:
        bridges = []
        
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            if not self.is_connected(V,node1, node2,adj):
                bridges.append((node1, node2))
            
        return bridges
    
        # 2. Check if d is reachable from c WITHOUT using the edge (c, d)
        # if self.is_connected(V, c, d, adj):
        #     # If still connected, it's NOT a bridge
        #     return 0
        # else:
        #     # If disconnected, it IS a bridge
        #     return 1
            
            

    def is_connected(self, V, start_node, target_node, adj):
        vis = [False] * V
        q = deque([start_node])
        vis[start_node] = True

        while q:
            node = q.popleft()
            
            # If we found the target, the path exists without the removed edge
            if node == target_node:
                return True

            for neigh in adj[node]:
                # Skip the specific edge we are testing
                if (node == start_node and neigh == target_node) or (node == target_node and neigh == start_node):
                    continue

                if not vis[neigh]:
                    vis[neigh] = True
                    q.append(neigh)
        
        return False
        
        
        
if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
    c = 1
    d = 3
    solution = Solution()
    print(solution.isBridge(V, edges, c, d))  
    # Output: 1 (since removing edge (1, 3) disconnects the graph)

    # [(1,3),(3,4)]
    