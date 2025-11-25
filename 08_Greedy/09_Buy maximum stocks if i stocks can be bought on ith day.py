

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        
        stocks = []
        
        for i in range(n):
            stocks.append((price[i], i+1))
            
        stocks.sort()
        count = 0
        
        for stock in stocks:
            p = stock[0]
            allowed = stock[1]
            
            if p <= k:
                for j in range(allowed, 0,-1):
                    if p * j <= k:
                        count += j
                        k -= p * j
                        break
                    
        return count
        
        
    def buyMaximumProducts_opt(self, n : int, k : int, price : List[int]) -> int:
        # code here
        
        stocks = []
        
        for i in range(n):
            stocks.append((price[i], i+1))
            
        stocks.sort()
        count = 0
        
        for stock in stocks:
            p = stock[0]
            allowed = stock[1]
            
            # max we can take k/p 
            # so take min of both
            max_take = k // p
            
            take = min(allowed, max_take)
            count += take
            
            k -= p * take
                    
        return count



if __name__ == "__main__":
    sol = Solution()

    # input:
    n = 5
    k = 20
    price = [10, 7, 19, 5, 3]

    # output: 6
    print(sol.buyMaximumProducts(n, k, price))  
    print(sol.buyMaximumProducts_opt(n, k, price))  