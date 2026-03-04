#User function Template for python3

# this is clockwise rotation. for anticlockwise rotate the column after finding transpose of matrix.

def rotate(mat): 
    #code here
    
    n = len(mat)
    
    # transpose: here we are running j from i+1 coz when i==j it means we are swapping elem with itself and when j < i it means we are again swapping elem which was previously swapped. so to avoid this we are running j from i+1.

    # transpose
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
            
    
    # reverse each row
    for i in range(n):
        reverse(mat[i])
    
    
def reverse(arr):
    si = 0
    ei = len(arr)-1
    
    while si <= ei:
        arr[si],arr[ei] = arr[ei],arr[si]
        si += 1
        ei -= 1
        
        
        

# input:
mat = [[1,2,3], [4,5,6], [7,8,9]]

rotate(mat)
# output:
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

print(mat)

