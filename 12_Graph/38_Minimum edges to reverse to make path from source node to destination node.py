from typing import List


from typing import List
from collections import deque

class Solution:
    def minimumEdgeReversal(self,edges : List[List[int]], n : int, m : int, src : int, dst : int) -> int:
        # code here
        
        adj = [[] for _ in range(n+1)]
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adj[node1].append((node2,0))
            adj[node2].append((node1,1))
        
        # now find minm cost path from source to dest
        q = deque()
        dist = [float("inf")]*(n+1)
        dist[src] = 0
        q.append(src)
        
        while q:
            node = q.popleft()
            
            for nn,edwt in adj[node]:
                if dist[nn] > dist[node] + edwt:
                    dist[nn] = dist[node] + edwt
                    q.append(nn)
        
        if dist[dst] == float("inf"):
            return -1
        
        return dist[dst]
        
        
                
        
if __name__ == "__main__":
    sol = Solution()

    edges = [[1, 2], [2, 3], [3, 4], [4, 5]]
    n = 5
    m = 4
    src = 1
    dst = 5
    print(sol.minimumEdgeReversal(edges, n, m, src, dst))  
    # Output: 0