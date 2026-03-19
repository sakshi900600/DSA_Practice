# User function Template for python3

from collections import deque

class Solution:
    def minSteps(self, m, n, d):
        # Code here
        if d > max(m, n):
            return -1
        
        q = deque()
        visited = set()
        q.append((0, 0, 0))
        visited.add((0, 0)) 
        
        while q:
            a, b, steps = q.popleft()
            
            if a == d or b == d:
                return steps
            
            # fill or empty jug1 or jug2
            next_steps = [(m, b), (a, n), (0, b), (a, 0)]
            
            # pour from jug1 -> jug2
            pour = min(a, n - b)
            next_steps.append((a - pour, b + pour))
            
            # pour from jug2 -> jug1
            pour = min(b, m - a)
            next_steps.append((a + pour, b - pour))
            
            for na, nb in next_steps:
                if (na, nb) not in visited:
                    visited.add((na, nb))
                    q.append((na, nb, steps + 1))
        
        return -1




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

    