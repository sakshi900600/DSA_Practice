#User function Template for python3
from typing import List

from collections import deque
class Solution:

    def CheapestFLight(self, n, flights, src, dst, k):
        
        adj = [[] for _ in range(n)]
        
        for x in flights:
            node1 = x[0]
            node2 = x[1]
            wt = x[2]
            adj[node1].append((node2, wt))
        
        q = deque()
        dist = [float('inf')]*n
        
        q.append((0,src,0)) # cost, node, stops
        dist[src] = 0
        
        while q:
            cost, node, stops = q.popleft()
            
            if stops > k:
                continue
            
            for x in adj[node]:
                neighn = x[0]
                edwt = x[1]
                
                if cost+edwt < dist[neighn] and stops <= k:
                    dist[neighn] = cost+edwt
                    q.append((cost+edwt, neighn, stops+1))
        
        
        if dist[dst] == float("inf"):
            return -1
        
        return dist[dst]
        
        
            
if __name__ == "__main__":
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    sol = Solution()
    print(sol.CheapestFLight(n,flights,src,dst,k))

    # Output: 200

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    print(sol.CheapestFLight(n,flights,src,dst,k))

    # Output: 500                 
            
            