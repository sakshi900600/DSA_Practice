#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self,str):
        #Write your code here
        n = len(str)
        
        count0 = 0
        count1 = 0
        
        count_substr = 0
        
        for i in str:
            if i == '0':
                count0 += 1
            else:
                count1 += 1
                
            if count0 == count1:
                count_substr += 1
                    
          
        # checking at last if full string can be our answer or not.
        if count0 != count1:
            return -1
        
            
        return count_substr
        


if __name__ == "__main__":
    sol = Solution()


    # input:
    S = "0100110101"
    # Output: 4

    print(sol.maxSubStr(S))
    