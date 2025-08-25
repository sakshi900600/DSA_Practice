def share_maxProfit(arr):
    n = len(arr)

    # [-1 for _ in range(3)] - list of cap=0,1,2
    # [[-1 for _ in range(3)] for _ in range(2)] - 2 for buy/sell option
    # n times row created.

#     dp = [
#   [[-1, -1, -1],
#    [-1, -1, -1]],

#   [[-1, -1, -1],
#    [-1, -1, -1]]
# ]


    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
    return helper(arr,0,1,2,dp)


def helper(arr,idx,buy,cap,dp):
    n = len(arr)
    
    if idx == n:
        return 0
    if cap == 0:
        return 0
    
    profit = 0
    if dp[idx][buy][cap] != -1:
        return dp[idx][buy][cap]

    if buy == 1: # we can buy
        profit = max(-arr[idx]+helper(arr,idx+1,0,cap,dp), 0+helper(arr,idx+1,1,cap,dp))
    else: # we can sell
        profit = max(arr[idx]+helper(arr,idx+1,1,cap-1,dp), 0 + helper(arr,idx+1,0,cap,dp))

    dp[idx][buy][cap] = profit

    return profit





# Input:   
prices = [10, 22, 5, 75, 65, 80]
# Output:  87


print(share_maxProfit(prices))