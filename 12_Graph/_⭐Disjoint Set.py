# Disjoin set is a data structure that keeps track of which node belongs to which components. 
# It has two main operations: find and union.
# find: it gives us ultimate parent of a node. if two nodes have same ultimate parent then they belong to same component.

# union: there are 2 ways for it: by rank, by size.

# union by rank: we connect smaller rank tree under bigger rank tree. if both have same rank then we can connect any one to other and increase the rank of that tree by 1.

# union by size: we connect smaller size tree under bigger size tree and update the size of bigger tree by adding the size of smaller tree.


# disjoint set union by rank
class DisjointSet1:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u,v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)

        if ulp_u == ulp_v:
            return
        
        # connect u to v
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        # connect v to u
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        # connect and update rank if have same rank to both ultimate parents
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        

# disjoint set union by size
class DisjointSet2:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u,v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)

        if ulp_u == ulp_v:
            return
        
        # connect u to v
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        # connect v to u
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]



def unionByRank():
    ds = DisjointSet1(7)
    ds.union(0,3)
    ds.union(1,2)
    ds.union(4,5)
    ds.union(5,6)
    ds.union(3,4)

    print(ds.parent)


def unionBySize():
    ds = DisjointSet2(7)
    ds.union(0,3)
    ds.union(1,2)
    ds.union(4,5)
    ds.union(5,6)
    ds.union(3,4)

    print(ds.parent)


if __name__ == "__main__":
    print("Union by rank: ")
    unionByRank()
    print("\nUnion by size: ")
    unionBySize()

    # Output:
    # Union by rank: 
    # [0, 1, 1, 0, 0, 4, 4]

    # Union by size:
    # [4, 1, 1, 0, 4, 4, 4]

        