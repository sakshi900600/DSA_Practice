edges = [[0, 1], [1, 2], [2, 0], [2, 3]]
V = 4

adjlist = [[] for _ in range(V)]

for x in edges:
    node1 = x[0]
    node2 = x[1]
    adjlist[node1].append(node2)


print(adjlist)
