from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        # using list - TLE ---------
        # i = 0
        # ans = []
        # n = len(arr)
        # for j in range(n):
        #     if j-i+1 == k:
        #         ans.append(max(arr[i:j+1]))
        #         i += 1
        # return ans


        # using deque - Optimized --------
        i = 0
        dq = deque()
        ans = []
        n = len(arr)
        
        for j in range(n):
            while dq and dq[-1] < arr[j]:
                dq.pop()
            dq.append(arr[j])
            
            if j-i+1 == k:
                ans.append(dq[0])
                
                if dq and arr[i] == dq[0]:
                    dq.popleft()
                
                i += 1
            
        return ans 
        


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3
    sol = Solution()
    print(sol.maxOfSubarrays(arr, k))  
    # Output: [3, 3, 4, 5, 5, 5, 6]

    
