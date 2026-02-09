# topological sort:  Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.


from collections import deque
class Solution:

    def topoSortdfs(self, V, edges):
        # Code here
        adjlist = [[]*V for _ in range(V)]
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            
            adjlist[node1].append(node2)    
        
        vis = [0]*V
        st = []
        
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i,vis,adjlist,st)
        
        topo = []
        while st:
            topo.append(st.pop())
            
        return topo
        
    
    def dfs(self, node, vis, adjlist,st):
        vis[node] = 1
        
        for neigh in adjlist[node]:
            if vis[neigh] == 0:
                self.dfs(neigh,vis,adjlist,st)
        
        st.append(node)
            
    # Khans Algorithm:
    # 1. find out indegree for each node. (indegree means how many nodes are coming on a particular node that will be its indegree)
    # put all node with 0 indegree into q
    # pop node & add in ans list and call for neighbors .
    # decrease their indegree by 1 and if becomes 0 then put in q 
    # at the end return ans list.
       
    def topoSortbfs(self, V, edges):
        # Code here
        adjlist = [[]*V for _ in range(V)]
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            
            adjlist[node1].append(node2)
            
        
        indegree = [0]*V
        
        for node in range(V):
            for neigh in adjlist[node]:
                indegree[neigh] +=1
        
        # bfs - khans algorithm
        q = deque()
        topo = []
        
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            topo.append(node)
            
            for neigh in adjlist[node]:
                indegree[neigh] -= 1
                
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        
        return topo
        


if __name__ == "__main__":
    V = 6
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    
    solution = Solution()
    topo_dfs = solution.topoSortdfs(V, edges)
    topo_bfs = solution.topoSortbfs(V, edges)

    print("Topological Sort (DFS):", topo_dfs)
    print("Topological Sort (BFS - Kahn's Algorithm):", topo_bfs)

    # Output:
    # Topological Sort (DFS): [5, 4, 2, 3, 1, 0]
    # Topological Sort (BFS - Kahn's Algorithm): [5, 4, 2, 3, 1, 0]

