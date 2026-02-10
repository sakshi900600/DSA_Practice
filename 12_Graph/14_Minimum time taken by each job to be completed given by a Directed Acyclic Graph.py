from typing import List
from collections import deque

# Logic:  Here also task first must be finished before performing second task. So indicating to topological sort. 

# Here we have to store minimum time for each task. So for all the tasks having indegree 0 will be all executed in 1 unit time. So store all tasks time in a list.

# Now, to update the adjacent tasks, we simply take time of its parent which calls current task and added 1 to it. coz here doing bfs so it automatically gurantees the minimum time.



class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        
        adjlist = [[]*(n+1) for _ in range(n+1)]
        indegree = [0]*(n+1)
        
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adjlist[node1].append(node2)
            indegree[node2] += 1
         
        time = [0]*(n+1)   
        
        q = deque()
        for i in range(n+1):
            if indegree[i] == 0:
                q.append(i)
                time[i] = 1
        
        while q:
            task = q.popleft()
            
            for next_task in adjlist[task]:
                indegree[next_task] -= 1
                
                if indegree[next_task] == 0:
                    time[next_task] = 1+time[task]
                    q.append(next_task)
        
        return time[1:]
                    
                    
                    
if __name__ == "__main__":

    sol = Solution()
    n = 7
    m = 7
    edges = [[1, 2], [2, 3], [2, 4], [2, 5], [3, 6], [4, 6], [5, 7]]
    print(sol.minimumTime(n, m, edges))  
    # Output: [1, 2, 3, 3, 3, 4, 4]
    

