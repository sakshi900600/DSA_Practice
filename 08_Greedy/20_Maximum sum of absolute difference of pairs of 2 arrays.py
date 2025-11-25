#User function Template for python3

class Solution:
    def findMinSum(self, A,B,N):
        
        A.sort()
        B.sort()
        
        sum = 0
        for i in range(N):
            sum += abs(A[i] - B[i])
        
        return sum

    

if __name__ == '__main__':
    sol = Solution()

    # input:
    A = [4,1,8,7]
    B = [2,3,6,5]
    N = len(A)

    # Output: 6
    print(sol.findMinSum(A, B, N))  