#User function Template for python3

class Solution:
    # TLE ------------
    def divide(self, dividend, divisor):
        #code here
        
        if dividend == 0:
            return 0
        
        sign = 1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
            
        return quotient * sign
    

    def divide_opt(self, a, b):
        #code here
        
        if a == -2**31 and b==-1:
            return 2**31-1
        
        sign = -1 if (a<0)^(b<0) else 1
        
        a = abs(a)
        b = abs(b)
        quotient = 0
        
        for i in range(31, -1, -1):
            if b<<i <= a:
                a -= b<<i
                quotient |= 1<<i
        
            
        return quotient * sign
        
        

if __name__ == "__main__":
    sol = Solution()

    a = 10
    b = 3
    print(sol.divide(a,b))
    print(sol.divide_opt(a,b))

    # Output: 3
