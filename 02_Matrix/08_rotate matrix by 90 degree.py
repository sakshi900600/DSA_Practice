#User function Template for python3

def rotate(mat): 
    #code here
    
    n = len(mat)
    
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
            
    
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

