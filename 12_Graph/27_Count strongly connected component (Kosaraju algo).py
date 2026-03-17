class Solution:

    def kosaraju(self, V, edges):
        # code here
        
        adj = [[] for _ in range(V)]
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adj[node1].append(node2)
        
        #step 1   
        st = []
        vis = [0]*V
        for i in range(V):
            if vis[i] == 0:
                self.dfs1(i,vis,st,adj)
        
        # step 2
        revadj = [[] for _ in range(V)]
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            revadj[node2].append(node1)
        
        # step 3
        ans = []
        vis = [0]*V # reinitalize
        while st:
            node = st.pop()
            if vis[node]== 0:
                li = []
                self.dfs2(node,vis,li,revadj)
                ans.append(li)
        
        return len(ans)
        
        
    def dfs1(self, node, vis, st,adj):
        vis[node] = 1
        
        for neigh in adj[node]:
            if vis[neigh] == 0:
                self.dfs1(neigh,vis,st,adj)
        
        st.append(node)
    
    
    def dfs2(self, node, vis, li, adj):
        vis[node] = 1
        li.append(node)
        
        for neigh in adj[node]:
            if vis[neigh] == 0:
                self.dfs2(neigh,vis,li,adj)

                
                
if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
    sol = Solution()
    print(sol.kosaraju(V,edges))

    # Output: 3

    V = 4
    edges = [[0, 1], [1, 2], [2, 3]]
    print(sol.kosaraju(V,edges))

    # Output: 4