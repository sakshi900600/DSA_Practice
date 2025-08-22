class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buyprice = prices[0]

        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] > buyprice:
                profit = prices[i] - buyprice
                maxProfit = max(maxProfit, profit)
            else:
                buyprice = prices[i]
        

        return maxProfit



if __name__ == "__main__":

    sol = Solution()

    # input:
    prices = [7,1,5,3,6,4]

    # output: 5
    
    print(sol.maxProfit(prices))