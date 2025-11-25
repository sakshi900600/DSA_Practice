class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        i = n-2
        
        while i>=0 and arr[i+1] <= arr[i]:
            i -= 1
            
        if i>=0:
            j = n-1
            while arr[j] <= arr[i]:
                j -= 1
                
            arr[i],arr[j] = arr[j],arr[i]
            
        
        start = i+1
        end = n-1
        
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
            
        
        return arr
        
        

if __name__ == "__main__":
    sol = Solution()

    # Input:
    arr = [2, 4, 1, 7, 5, 0]
    # Output: [2, 4, 5, 0, 1, 7]

    print(sol.nextPermutation(arr))