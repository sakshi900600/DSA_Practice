# count and say series starts from 1 and then we read the previous number and say how many times it occurs and what number it is. 
# ex: 1 is read as "one 1" which is 11

# so if number = n then we read the (n-1)th term and that becomes nth term.

# 1st term = 1 (bc)
# 2nd term = 11 (one 1)
# 3rd term = 21 (two 1)
# 4th term = 1211 (one 2, one 1)
# 5th term = 111221 (one 1, one 2, two 1)


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        res = "1"
        for _ in range(n-1):
            newStr = ""
            count = 1

            for i in range(1,len(res)):
                if res[i]==res[i-1]:
                    count += 1
                else:
                    newStr += str(count)+res[i-1]
                    count = 1
            
            # at the end some count may left and never go to else so add that in newStr
            newStr +=  str(count)+res[-1]
        
            res = newStr

        return res
        

if __name__ == "__main__":

    sol = Solution()
    n = 4
    print(sol.countAndSay(n))
    # Output: 1211
    