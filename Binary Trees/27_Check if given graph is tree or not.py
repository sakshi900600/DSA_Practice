class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def dfs(node, visited, adjList, parent):
    visited[node] = True

    for adjNode in adjList[node]:
        if not visited[adjNode]:
            if dfs(adjNode, visited, adjList, node):
                return True
        elif adjNode != parent:
            return True

    return False


def isCycle(V, adjList, visited):
    for i in range(V):
        if not visited[i]:
            if dfs(i, visited, adjList, -1):
                return True
    return False



def isTree(V, adjList):
    visited = [False] * V

    if isCycle(V, adjList, visited):
        return False

    # checking if graph is fully connected or in form of components
    for i in range(V):
        if not visited[i]:
            return False

    return True



if __name__ == '__main__':
    # create adjacency list from edges
    edges = [[1, 0], [2, 0], [3, 0], [3, 4]]
    V = 5  # number of vertices
    adjList = [[] for _ in range(V)]

    def add_edges(edges):
        for x in edges:
            node1 = x[0]
            node2 = x[1]
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        return adjList

    add_edges(edges)

    

    # output: True
    print(isTree(V, adjList))
