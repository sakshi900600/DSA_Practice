class Solution:

    def pathMoreThanK(self, V, edges, K, src):
        # code here
        
        adj = [[] for _ in range(V)]
        
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            wt = x[2]
            
            adj[node1].append((node2, wt))
            adj[node2].append((node1, wt))
        
        vis = [0]*V
        
        
        def dfs(node, curr_cost):
            if curr_cost >= K:
                return True
            
            vis[node] = 1
            
            for nn,edwt in adj[node]:
                if vis[nn] == 0:
                    if dfs(nn,curr_cost+edwt):
                        return True
            
            vis[node] = 0
            return False
        
        
        return dfs(src,0)
                
            

if __name__ == "__main__":
    V = 9
    edges = [
        [0, 1, 4], [0, 7, 8], [1, 7, 11],
        [1, 2, 8], [2, 8, 2], [8, 6, 6],
        [6, 7, 1], [7, 8, 7], [2, 3, 7],
        [2, 5, 4], [5, 6, 2], [3, 5, 14],
        [3, 4, 9], [4, 5, 10]
    ]
    src, k = 0, 58

    sol = Solution()
    print(sol.pathMoreThanK(V, edges, k, src))
    # Output: True


    src = 0
    k = 62
    V = 9
    edges = [[0, 1, 4], [0, 7, 8], [1, 7, 11], [1, 2, 8], [2, 8, 2], [8, 6, 6], [6, 7, 1], [7, 8, 7], [2, 3, 7], [2, 5, 4], [5, 6, 2], [3, 5, 14], [3, 4, 9], [4, 5, 10]]

    print(sol.pathMoreThanK(V,edges,k,src))
    # Output: False

    