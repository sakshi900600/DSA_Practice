
def minJumps(arr):
    n = len(arr)

    if n == 1:
        return 0
    
    if arr[0] == 0:
        return -1
    
    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1,n):
        if i==n-1:
            return jumps
        
        max_reach = max(max_reach, i+arr[i])

        steps -= 1

        if steps == 0:
            jumps += 1

            if i >= max_reach:
                return -1
            
            steps = max_reach - i
    
    return -1



def min_jumps(arr):
    n = len(arr)

    if n == 0 or a[0]==0:
        return -1
    
    dp = [float('inf')]*n

    dp[0] = 0

    for i in range(n):
        if dp[i] != float('inf'):
            max_steps = a[i]

            for j in range(1,max_steps):
                if (i+j) < n:
                    dp[i+j] = min(dp[i+j], dp[i]+1)
    
    return -1 if dp[n-1]==float('inf') else dp[n-1]



# input:
a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# output: 3

# print(minJumps(a))
print(min_jumps(a))




