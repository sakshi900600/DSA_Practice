# here we have to divide graph into 2 parts such that in each group nodes must be connected to each other. 

# In bipartite there also divide graph into 2 parts but there both groups nodes are not connected to each other internally.

# so we will take transpose of graph and pass to bipartite fun and return its ans


from collections import deque
def isBipartite(adj, n):

    colors = [-1]*n

    for i in range(n):
        if colors[i] == -1:
            # bfs
            q = deque()
            q.append(i)
            colors[i] = 0

            while q:
                node = q.popleft()

                for neigh in adj[node]:
                    if colors[neigh] == -1:
                        colors[neigh] = 1-colors[node]
                        q.append(neigh)
                    elif colors[node] == colors[neigh]:
                        return False
    
    return True



def two_clique(adjmat):
    n = len(adjmat)
    # complement of mat:
    comp_adj = [[] for _ in range(n)]

    # given mat will be square mat
    for i in range(n):
        for j in range(n):
            if i!=j and adjmat[i][j]==0:
                comp_adj[i].append(j)

    return isBipartite(comp_adj, n)



if __name__ == "__main__":
    G = [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    if two_clique(G):
        print("Yes")
    else:
        print("No")


    # Output: Yes

