

from typing import List


class Solution:
    def maxEqualSum(self, N1:int,N2:int,N3:int, s1 : List[int], s2 : List[int], s3 : List[int]) -> int:
        # code here
        
        suffix3 = [0]* (N3+1)
        
        # suffix sums of stack 1
        sum1 = 0
        st1 = set()
        
        for i in range(N1-1, -1, -1):
            sum1 += s1[i]
            st1.add(sum1)
            
        # suffix sums of stack 2
        sum2 = 0
        st2 = set()
        
        for i in range(N2-1, -1, -1):
            sum2 += s2[i]
            st2.add(sum2)
        
        
        # suffix sums of stack 3
        for i in range(N3-1, -1, -1):
            suffix3[i] = suffix3[i+1] + s3[i]
        
        
        # checking the max suffix sum in all 3
        for i in range(len(suffix3)):
            if suffix3[i] in st1 and suffix3[i] in st2:
                return suffix3[i]
        
        
        return 0
        
        
        
        
if __name__ == "__main__":
    sol = Solution()
    N1 = 5
    N2 = 3
    N3 = 4
    s1 = [3, 2, 1, 1, 1]
    s2 = [4, 3, 2]
    s3 = [1, 1, 4, 1]

    # Output: 5
    print(sol.maxEqualSum(N1, N2, N3, s1, s2, s3))          
