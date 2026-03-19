def oliver(n, edges, query):
    adj = [[] for _ in range(n+1)]

    for x,y in edges:
        adj[x].append(y)
        adj[y].append(x)

    in_time = [0]*(n+1)
    out_time = [0]*(n+1)
    timer = 0

    def dfs(node, parent):
        nonlocal timer
        in_time[node] = timer
        timer += 1

        for neigh in adj[node]:
            if neigh != parent:
                dfs(neigh,node)
        
        out_time[node] = timer
        timer += 1


    dfs(1, -1)

    def is_ancestor(x,y):
        return in_time[x] <= in_time[y] and out_time[x] >= out_time[y]
    
    # forward/backward, olive, bob
    dir = query[0]
    x = query[1]
    y = query[2]

    if dir == 1:
        x,y = y,x

    return is_ancestor(x,y)



if __name__ == "__main__":

    n = 9
    edges = [(1,2),(1,3),(2,6),(2,7),(6,9),(7,8),(3,4),(3,5)]
    # query = [0,2,8] # True
    # query = [1,2,8] # False
    query = [1,9,1] # True

    print(oliver(n, edges, query))  

