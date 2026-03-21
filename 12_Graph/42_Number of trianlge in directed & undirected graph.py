def triangle_dir_undir(adj, isdirected):
    n = len(adj)

    tri_count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and j!=k and i!=k and adj[i][j] and adj[j][k] and adj[k][i]:
                    tri_count += 1
    

    # in directed edge we will visit same triangle 3 times, so divide by 3 
    # in undirected edge we will visit same triangle 6  times, so divide by 6 
    if isdirected:
        return tri_count //3
    else:
        return tri_count//6



# Create adjacency matrix of an undirected graph
graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]
# Create adjacency matrix of a directed graph
digraph = [[0, 0, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 0, 0],
           [0, 0, 1, 0]]


print(triangle_dir_undir(graph, False)) # 2
print(triangle_dir_undir(digraph, True)) # 2

