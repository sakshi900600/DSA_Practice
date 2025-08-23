#User function Template for python3

class Solution:
    def factorial(self, n):
        #code here
        
        fact = self.fact_helper(n) # number
        fact_str = str(fact)
        
        ans = list(fact_str)
        
        return ans
        
        
    
    def fact_helper(self,n):
        if n == 1:
            return 1
        
        return n*self.fact_helper(n-1)
    


if __name__ == "__main__":

    sol = Solution()

    # input: 5
    # output: ['1', '2', '0']
    
    print(sol.factorial(5))