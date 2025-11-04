# The ques given of this link is something else.



class Solution:
    def findMin(self, n):
       # code here 
        coins = [10,5,2,1]
       
        total_coins = 0
       
        for coin in coins:
            if coin <= n:
               total_coins += n // coin
               n = n % coin
               
        
        return total_coins
       

if __name__ == '__main__':

    # Input: 
    n = 121

    # Output: 13
    sol = Solution()
    print(sol.findMin(n))