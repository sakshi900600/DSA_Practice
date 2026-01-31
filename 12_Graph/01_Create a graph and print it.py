
# 1. using adjacency matrix  
def create_graph_mat(edges, V):
    adjmat = [[0]*V for _ in range(V)]

    for x in edges:
        node1 = x[0]
        node2 = x[1]
        adjmat[node1][node2] = 1
        adjmat[node2][node1] = 1
    
    return adjmat


# 2. using adjacency list
def create_graph_list(edges, V):
    adjlist = [[] for _ in range(V)]

    for x in edges:
        node1 = x[0]
        node2 = x[1]
        adjlist[node1].append(node2)
        adjlist[node2].append(node1)
    
    return adjlist



if __name__ == "__main__":
    edges = [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4)]
    V = 5

    print("Adjacency Matrix:")
    graph_mat = create_graph_mat(edges, V)
    for row in graph_mat:
        print(row)

    print("\nAdjacency List:")
    graph_list = create_graph_list(edges, V)
    for idx, neighbors in enumerate(graph_list):
        print(f"{idx}: {neighbors}")


    # Output:
    # Adjacency Matrix:
    # [0, 1, 0, 0, 1]
    # [1, 0, 1, 1, 1]
    # [0, 1, 0, 1, 0]
    # [0, 1, 1, 0, 1]
    # [1, 1, 0, 1, 0]

    # Adjacency List:
    # 0: [1, 4]
    # 1: [0, 4, 3, 2]
    # 2: [1, 3]
    # 3: [1, 2, 4]
    # 4: [0, 1, 3]
