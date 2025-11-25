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










# use the logic of buy and sell stock

def maxProfitOne(prices,idx):

    buy = prices[idx]
    maxProfit = 0

    for i in range(idx+1, len(prices)):
        if prices[i] > buy:
            profit = prices[i] - buy
            maxProfit = max(maxProfit, profit)
        else:
            buy = prices[i]

    return maxProfit



def maxProfit(prices):
    n = len(prices)

    buy = prices[0]
    maxProfit = 0

    for i in range(1,n):
        if prices[i] > buy:
            profit = prices[i] - buy + maxProfitOne(prices, i)
            maxProfit = max(maxProfit, profit)
        else:
            buy = prices[i]

    
    return maxProfit






def maxProfit_dp(prices):
    
    # Variables to store the maximum profit 
    # after the first and second transactions
    firstBuy = float('-inf')  
    firstSell = 0      
    secondBuy = float('-inf') 
    secondSell = 0      
    
    # Iterate over each day's stock prices
    for i in range(len(prices)):
        
        # Calculate maximum profit
        firstBuy = max(firstBuy, -prices[i])
        firstSell = max(firstSell, firstBuy + prices[i])
        secondBuy = max(secondBuy, firstSell - prices[i])
        secondSell = max(secondSell, secondBuy + prices[i])
    
    # The result is the maximum 
    # profit after the second sell
    return secondSell

if __name__ == "__main__":
    prices = [10, 22, 5, 75, 65, 80]
    print(maxProfit_dp(prices))











# Input:   
prices = [10, 22, 5, 75, 65, 80]
# Output:  87


# print(share_maxProfit(prices))

print(maxProfit(prices))