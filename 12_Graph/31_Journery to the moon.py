
# tle -----
def journeyToMoon(n, astronaut):
    # Write your code here
    adj = [[] for _ in range(n)]
    
    for x in astronaut:
        node1 = x[0]
        node2 = x[1]
        
        adj[node1].append(node2)
        adj[node2].append(node1)
    
    vis = [0]*n
    comp_node_cnts = []
    
    for i in range(n):
        if vis[i] == 0:
            nodecnt = [0]
            dfs(i,vis,adj,nodecnt)
            comp_node_cnts.append(nodecnt[0])
    
    res = 0
    for i in range(len(comp_node_cnts)):
        num = comp_node_cnts[i]
        for j in range(i+1, len(comp_node_cnts)):
            res += num * comp_node_cnts[j]
    
    return res
        
    
def dfs(node, vis, adj, nodecnt):
    vis[node] = 1
    nodecnt[0] += 1
    
    for neigh in adj[node]:
        if vis[neigh] == 0:
            dfs(neigh, vis, adj, nodecnt)



def journeyToMoon(n, astronaut):

    adj = [[] for _ in range(n)]

    for u, v in astronaut:
        adj[u].append(v)
        adj[v].append(u)

    vis = [0] * n
    comp_sizes = []

    for i in range(n):
        if vis[i] == 0:
            size = dfs(i, vis, adj)
            comp_sizes.append(size)

    res = 0
    running_sum = 0

    for size in comp_sizes:
        res += running_sum * size
        running_sum += size

    return res


def dfs(node, vis, adj):

    vis[node] = 1
    count = 1

    for neigh in adj[node]:
        if vis[neigh] == 0:
            count += dfs(neigh, vis, adj)

    return count


