# Kruskals algo: It is used to find MST. 
# 1. sort edges based on wt in asc order.
# 2. for each edge check if both u and v belongs to same component or not. if they belongs then it means if we take current edge then cycle will be formed. 
# For checking if they belong to same component or not we use disjoint set. 
# if they belongs to different component then we can take this edge and add wt in total cost and also do union of both components.

# at the end return min cost of spanning tree.



#User function Template for python3
from typing import List

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        # sort edges based on weight in asc order
        edges.sort(key=lambda x: x[2])
        
        cost = 0
        mst_edges = []
        ds = disjointset(V)
        
        for u,v,w in edges:
            if ds.union(u,v):
                cost += w
                mst_edges.append((u,v,w))
        
        return cost
    
    
class disjointset:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pu == pv:
            return False
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        
        return True
        
        
        
if __name__ == "__main__":
    V = 3
    E = 3
    edges = [[0,1,5],[1,2,3],[0,2,1]]
    sol = Solution()
    print(sol.kruskalsMST(V,edges))

    # Output: 4

