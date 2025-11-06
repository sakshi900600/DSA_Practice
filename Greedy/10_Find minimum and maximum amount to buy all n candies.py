class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        n = len(prices)
        prices.sort()
        mini = 0
        maxi = 0
        
        # finding mini
        start = 0
        end = n-1
        while start <= end:
            mini += prices[start]
            start += 1
            end -= k
        
        # finding maxi
        start = n-1
        end = 0
        
        while start >= end:
            maxi += prices[start]
            start -= 1
            end += k
            
        
        
        return [mini, maxi]
        
        

if __name__ == "__main__":
    prices = [3, 2, 1, 4]
    k = 2
    sol = Solution()

    # Output: [3, 7]
    print(sol.minMaxCandy(prices, k))  