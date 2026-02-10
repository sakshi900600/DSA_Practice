from collections import deque

# Here if cycle exists then all tasks can't be finished otherwise we can finish all the tasks.
# so first approach - I have checked if cycle exists in directed graph. If yes means not possible.

# second approach - Topological sort
# Here if cycle exists then we can't do topological sort and if we can do topological sort then we can finish all the tasks. So I have used khans algo. At the end checked if any node has indegree > 0 then return False otherwise True.


class Solution:
    def canFinish(self, n, prerequisites):
        # code here 
        adjlist = [[]*n for _ in range(n)]
        
        for x in prerequisites:
            node2 = x[0]
            node1 = x[1]
            adjlist[node1].append(node2)
            
        return not self.isCycle(adjlist)
    
    
    def isCycle(self, adjlist):
        n = len(adjlist)
        
        vis = [0]*n
        active = [0]*n
        
        for i in range(n):
            if vis[i] == 0:
                if self.dfs(i, vis,active,adjlist):
                    return True
        
        return False
        
    def dfs(self,node,vis,st,adjlist):
        vis[node] = 1
        st[node] = 1
        
        for neigh in adjlist[node]:
            if vis[neigh] == 0:
                if self.dfs(neigh, vis, st, adjlist):
                    return True
            elif vis[neigh]==1 and st[neigh]==1:
                return True
        
        st[node] = 0
        return False
        

    # Using topological Sort - Khans algo
    def canFinish_topo(self, n, prerequisites):
        # code here 
        adjlist = [[]*n for _ in range(n)]
        indegree = [0]*n
        
        for x in prerequisites:
            node2 = x[0]
            node1 = x[1]
            adjlist[node1].append(node2)
            indegree[node2] += 1
        
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            
            for neigh in adjlist[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        for i in range(n):
            if indegree[i] != 0:
                return False
        
        return True
    


if __name__ == "__main__":
    n = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    
    solution = Solution()
    print(solution.canFinish(n, prerequisites))  
    # Output: True
    
    n = 2
    prerequisites = [[1,0],[0,1]]
    
    print(solution.canFinish(n, prerequisites))  
    # Output: False

    




        
        