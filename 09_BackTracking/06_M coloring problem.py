# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        
        adjList = [[] for i in range(v)]
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
            
        color_arr = [-1]*v
        
        
        def helper(node):
            if node == v:
                return True
            
            for c in range(m):
                if self.isSafe(node, c, color_arr, adjList):
                    color_arr[node] = c
                    if helper(node+1):
                        return True
                    color_arr[node] = -1
            
            return False
            
        return helper(0)
        
        
    
    def isSafe(self, node, col,color_arr, adjList):
        for adjNode in adjList[node]:
            if color_arr[adjNode] != -1 and  color_arr[adjNode] == col:
                return False
                
        return True
    


if __name__ == "__main__":
    sol = Solution()

    # Input:
    v = 4
    m = 3
    edges = [[0, 1], [1, 3], [2, 3], [3, 0], [0, 2]]

    print(sol.graphColoring(v, edges, m))
    # Output:  True