#User function Template for python3

import heapq
from typing import List
class Solution:
    def minCashFlow(self, transaction: List[List[int]], n: int) -> List[List[int]]:
        #code here
        
        # step1: find net profit (net profit = total_take(j,i) - total_give(i,j) )
        net_profit = [0]*n
        
        for i in range(n):
            for j in range(n):
                net_profit[i] += transaction[j][i] - transaction[i][j]
        
        
        # step2: seperate pos and neg values
        debtors = []
        creditors = []
        
        for idx, amt in enumerate(net_profit):
            if amt < 0:
                heapq.heappush(debtors, (amt, idx))
            else:
                # storing negative value to make max heap
                heapq.heappush(creditors, (-amt, idx))
                
        
        # step3: minimize transcation and store res
        result = [[0]*n for _ in range(n)]
        
        while debtors and creditors:
            damt, did = heapq.heappop(debtors)
            camt, cid = heapq.heappop(creditors)
            
            damt = -damt
            camt = -camt
            
            # find min transfer amount
            transfer = min(damt, camt)
            result[did][cid] = transfer
            
            damt -= transfer
            camt -= transfer
            
            if damt > 0:
                heapq.heappush(debtors, (-damt, did))
            
            if camt > 0:
                heapq.heappush(creditors, (-camt, cid))
        
        
        return result
            
        
        
if __name__ == "__main__":
    # Input:
    transactions = [
        [0, 1000, 2000],
        [0, 0, 5000],
        [0, 0, 0]
    ]
    n = 3

    sol = Solution()
    result = sol.minCashFlow(transactions, n)
    for row in result:
        print(row)

    # Output:
    # [0, 0, 3000]
    # [0, 0, 4000]
    # [0, 0, 0]
                
