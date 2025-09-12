#User function Template for python3

class Solution:

    # tle -------------------
    def productExceptSelf(self, arr):
        #code here
        
        n = len(arr)
        
        ans = [0]*n
        
        for i in range(n):
            product = 1
            curr_idx = i
            
            for j in range(n):
                if j == curr_idx:
                    continue
                
                product *= arr[j]
            ans[i] = product
            
        return ans
    



if __name__ == "__main__":
    sol = Solution()

    # input:
    arr = [10, 3, 5, 6, 2]
    # Output: [180, 600, 360, 300, 900]

    print(sol.productExceptSelf(arr))