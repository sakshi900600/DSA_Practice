#            1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1



class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = []
        for i in range(numRows):
            li = []
            for j in range(i+1):
                if j==0 or j==i:
                    li.append(1)
                else:
                    val = ans[i-1][j-1] + ans[i-1][j]
                    li.append(val)

            ans.append(li)

        return ans

        

sol = Solution()
# print(sol.generate(5))
