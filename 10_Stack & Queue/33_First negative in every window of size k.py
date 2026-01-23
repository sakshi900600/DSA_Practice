#User function Template for python3
from collections import deque

class Solution:
    def firstNegInt(self, arr, k): 
         # code here 
        n = len(arr)
        q = deque()
        i = 0
        j = 0
        
        ans = []
        
        while j < n:
            if arr[j] < 0:
                q.append(arr[j])
                
            if j-i+1 == k:
                if not q:
                    ans.append(0)
                else:
                    ans.append(q[0])
                
                if q and arr[i] == q[0]:
                    q.popleft()
                i += 1
            
            j += 1
        
        
        return ans
                    


if __name__ == "__main__":
    sol = Solution()

    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    print(sol.firstNegInt(arr,k))

    # Output:
    # [-1, -1, -7, -15, -15, 0]