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
    



    # coz factorial of a large number can be so large that it can't be stored in 
    # multiplying list with a number
    def multiply_List(self,a,num):
        i = len(a) -1

        carry = 0
        while i>=0 :
            value = num* a[i] + carry
            a[i] = value%10 
            carry = value //10
            i -= 1

        while carry > 0:
            a.insert(0,carry%10)
            carry = carry //10

        return a
    

    # factorial of  a large number:
    def factorial(self,number):
        if number == 0:
            return 1
        a = [1]

        for i in range(1,number+1):
            self.multiply_List(a,i)
        
        return a


            


    


if __name__ == "__main__":

    sol = Solution()

    # input: 5
    # output: ['1', '2', '0']
    
    # print(sol.factorial(5))


    # a = [1,2,3,4,5,6]
    # a.insert(0,9)

    # print(sol.multiply_List(a,8))
    # print(sol.multiply_List(a,190))

    print(sol.factorial(0))

    