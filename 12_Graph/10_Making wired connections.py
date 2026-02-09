# Approach:  
# In order to connect c computers we will need minimum c-1 wires.
# So if total wires is more than what we need to connect then thats extra wire, which we can use to connect other non-connected computers

# To find connected components - used dfs and counted whenever call for dfs
# to get extra edges use this formula:
#  [total_edges - (nodes - components)]

# if we have enough extra edges then we can definately connect and minimum will be c-1 wires otherwise not possible. 


class Solution(object):
    
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        adjlist = [[]*n for _ in range(n)]
        for edge in connections:
            node1 = edge[0]
            node2 = edge[1]

            adjlist[node1].append(node2)
            adjlist[node2].append(node1)
        
        vis = [0]*n
        component = 0 # no of components
        for i in range(n):
            if vis[i] == 0:
                component += 1
                self.dfs(i, vis, adjlist)
        
        min_req_edges = component - 1
        total_edges = len(connections)

        extra_edges = total_edges -(n-component)

        if extra_edges >= min_req_edges:
            return min_req_edges
        
        return -1


    def dfs(self, node, vis, adjlist):
        vis[node] = 1

        for neigh in adjlist[node]:
            if vis[neigh] == 0:
                self.dfs(neigh, vis, adjlist)

        
        

if __name__ == "__main__":
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    solution = Solution()
    print(solution.makeConnected(n, connections)) 
    # Output: 1

    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2]]
    print(solution.makeConnected(n, connections)) 
    # Output: -1

