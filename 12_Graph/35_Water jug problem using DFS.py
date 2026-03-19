# User function Template for python3

class Solution:
    # works but TLE, bfs will work fine here.
    def minSteps(self, m, n, d):
        # Code here
        if d > max(m, n):
            return -1
        
        vis = set()
        min_steps = [float("inf")]
        self.dfs(0, 0, m, n, 0, vis, d, min_steps)
        
        if min_steps[0] == float("inf"):
            return -1
        
        return min_steps[0]
        
    def dfs(self, a, b, m, n, step, vis, d, min_steps):
        if min_steps[0] <= step:
            return
        
        if a == d or b == d:
            min_steps[0] = min(min_steps[0], step)
            return
        
        # fill or empty jug1 or jug2
        next_steps = [(m, b), (a, n), (0, b), (a, 0)]
        
        # pour from jug1 -> jug2
        pour = min(a, n - b)
        next_steps.append((a - pour, b + pour))
        
        # pour from jug2 -> jug1
        pour = min(b, m - a)
        next_steps.append((a + pour, b - pour))
        
        vis.add((a, b))
        
        for na, nb in next_steps:
            if (na, nb) not in vis:
                self.dfs(na, nb, m, n, step + 1, vis, d, min_steps)
        
        vis.remove((a, b))




if __name__ == "__main__":
    m = 5
    n = 3
    d = 4
    sol = Solution()
    print(sol.minSteps(m, n, d))  # Output: 6

    m = 2
    n = 6
    d = 5
    print(sol.minSteps(m, n, d))  # Output: -1

    