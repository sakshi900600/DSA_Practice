
# TLE: ----------
class Solution:
    def tsp(self, cost):
        n = len(cost)
        vis = [0] * n
        vis[0] = 1
        return self.dfs(cost, vis, 0, 1)

    def dfs(self, cost, vis, last, cnt):
        n = len(cost)
        
        if cnt == n:
            return cost[last][0]
            
        minCost = float("inf")
        
        for city in range(1, n):
            if vis[city] == 0:
                vis[city] = 1
                minCost = min(minCost, cost[last][city] + self.dfs(cost, vis, city, cnt + 1))
                vis[city] = 0
        
        return minCost
    

