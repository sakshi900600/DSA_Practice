# 1. create adjlist
# 2. start with any node , put wt,node in min-heap(pq).
# 3. everytime pop from pq and then mark visited and add wt in total cost. 
# imp: Do not mark while putitng in queue, mark only when removing from pq. coz when we are putting all neigh in pq it means we have these options but we have to choose min wt edge and that we get when we pop .


import heapq
class Solution:
    def spanningTree(self, V, edges):
        # code here
        adjlist = [[] for _ in range(V)]
        
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            wt = x[2]
            adjlist[node1].append((node2,wt))
            adjlist[node2].append((node1,wt))
            
        pq = []
        vis = [0]*V
        cost = 0
        heapq.heappush(pq,(0,0))
        
        while pq:
            wt,node = heapq.heappop(pq)
            
            if vis[node] == 1:
                continue
            
            cost += wt
            vis[node] = 1
            
            for x in adjlist[node]:
                neigh_node = x[0]
                edge_wt = x[1]
                heapq.heappush(pq,(edge_wt,neigh_node))
        
        return cost
            
        
        
if __name__ == "__main__":
    V = 3
    E = 3
    edges = [[0,1,5],[1,2,3],[0,2,1]]
    sol = Solution()
    print(sol.spanningTree(V,edges))

    # Output: 4

    