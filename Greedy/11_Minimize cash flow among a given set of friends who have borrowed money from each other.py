






transaction = [[0,1000,200], [0,0,5000], [0,0,0]]

n = len(transaction)
# storing (give, receive)
trans_det = [[0]*2 for i in range(n)]
        
for i in range(n):
    give = 0
    receive = 0 
    for j in range(n):
        give -= transaction[i][j]
        trans_det[j][1] += transaction[i][j]
    
    trans_det[i][0] = give
        
print(trans_det)