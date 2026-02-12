# Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in the graph, even if the graph contains negative weight edges. It can also detect negative weight cycles in the graph.

#User function Template for python3

class Solution:
    def isNegativeWeightCycle(self, n, edges):
        #Code here
        
        dist = [float('inf')] * n
        
        # here we are taking each node as source and checking for negative cycle.
        for source in range(n):
            # for first source dist will be updated so for next sources we have to reinitailize dist array.
            dist = [float('inf')] * n
            dist[source] = 0
        
            # relax edges n-1 times
            for i in range(n - 1):
                for u, v, w in edges:
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            
            # detect negative cycles: if any dist gets updated again then cycle exists
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    return 1
        
        return 0
    


if __name__ == "__main__":
    n = 3
    edges = [[0,1,5],[1,2,-2],[0,2,1]]
    sol = Solution()
    print(sol.isNegativeWeightCycle(n,edges))

    # Output: 0

    n = 3
    edges = [[0,1,-1],[1,2,-2],[2,0,-3]]
    print(sol.isNegativeWeightCycle(n,edges))

    # Output: 1

