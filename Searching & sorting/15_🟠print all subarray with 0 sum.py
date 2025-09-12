class Solution:

    # tle --------------
    def findSubarray(self, arr):
        #code here.
        
        total = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i,n):
                subarr_sum = sum(arr[i:j+1])
                
                if subarr_sum == 0:
                    total += 1
                    
        
        return total
    



if __name__ == "__main__":
    sol = Solution()

    # input:
    arr = [0, 0, 5, 5, 0, 0]
    # Output: 6

    print(sol.findSubarray(arr))