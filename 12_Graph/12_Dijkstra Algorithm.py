import heapq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adjlist = [[] for _ in range(V)]
        
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            wt = x[2]
            
            adjlist[node1].append((node2,wt))
            adjlist[node2].append((node1,wt))
            
        
        return self.bfs(src, adjlist)
        
    
    def bfs(self, src, adjlist):
        n = len(adjlist)
        
        min_heap = []
        dist = [float('inf')] * n
        
        dist[src] = 0
        
        heapq.heappush(min_heap, (0,src))
        
        while min_heap:
            ds, node = heapq.heappop(min_heap)
            
            for x in adjlist[node]:
                adjnode = x[0]
                adjwt = x[1]
                
                if ds+adjwt < dist[adjnode]:
                    dist[adjnode] = ds+adjwt
                    heapq.heappush(min_heap, (ds+adjwt,adjnode))
        
        
        return dist
        
        

if __name__ == "__main__":
    V = 5
    edges = [
        [0, 1, 9],
        [0, 2, 6],
        [0, 3, 5],
        [0, 4, 3],
        [2, 1, 2],
        [2, 3, 4]
    ]
    src = 0

    solution = Solution()
    distances = solution.dijkstra(V, edges, src)
    print(src, ":", distances)

    # Output: 0 : [0, 8, 6, 5, 3]

    