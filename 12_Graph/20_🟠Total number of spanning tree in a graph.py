

def build_adjmat(n, edges):
    adjmat = [[0]*n for _ in range(n)]
    for u, v in edges:
        adjmat[u][v] += 1  
        adjmat[v][u] += 1
    return adjmat


def build_degree(n, adjmat):
    degree = [[0]*n for _ in range(n)]
    for i in range(n):
        degree[i][i] = sum(adjmat[i])
    return degree


def build_laplacian(adjmat, degree, n):
    lap = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            lap[i][j] = degree[i][j] - adjmat[i][j]
    return lap


# Remove last row and column for Laplacian reduction
def reduce_laplacian(lap, n):
    reduced = []
    for i in range(n-1):
        row = []
        for j in range(n-1):
            row.append(lap[i][j])
        reduced.append(row)
    return reduced



def determinant(mat):
    n = len(mat)
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    
    det = 0
    for c in range(n):
        # Create minor matrix
        minor = []
        for i in range(1, n):
            row = []
            for j in range(n):
                if j != c:
                    row.append(mat[i][j])
            minor.append(row)
        sign = (-1)**c
        det += sign * mat[0][c] * determinant(minor)
    return det



if __name__ == "__main__":
    n = 3
    # Remove duplicate edges - each edge should appear once
    edges = [[0,1], [0,2], [1,2]]  # Complete graph K3
    
    adjmat = build_adjmat(n, edges)
    degree = build_degree(n, adjmat)
    laplacian = build_laplacian(adjmat, degree, n)
    
    print("Laplacian Matrix:")
    print(laplacian)
    
    reduced = reduce_laplacian(laplacian, n)
    print("\nReduced Laplacian:")
    print(reduced)
    
    result = determinant(reduced)
    print(f"\nNumber of spanning trees: {result}")
    
    # For K3 (complete graph with 3 vertices), 
    # number of spanning trees = 3^(3-2) = 3

    # Output:
    # Laplacian Matrix:
    # [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]

    # Reduced Laplacian:
    # [[2, -1], [-1, 2]]

    # Number of spanning trees: 3

