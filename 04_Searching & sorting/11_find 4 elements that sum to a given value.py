class Solution:
    def fourSum(self, arr, target):
        # code here
        
        arr.sort()
        
        n = len(arr)
        ans = []
        
        for i in range(n):
            if i!=0 and arr[i]== arr[i-1]:
                continue
            
            for j in range(i+1, n):
                
                if j!=i+1 and arr[j] == arr[j-1]:
                    continue
                
                l = j+1
                r = n-1
                
                while l<r:
                    sum = arr[i]+ arr[j]+arr[l]+arr[r]
                    
                    if sum == target:
                        ans.append([arr[i],arr[j],arr[l],arr[r]])
                        
                        l += 1
                        r -= 1
                        
                        while l<r and arr[l] == arr[l-1]:
                            l += 1
                        while l<r and arr[r] == arr[r+1]:
                            r -= 1
                        
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
                        
                        
        
        return ans
                        
                        
                        
                        
                        
                        
                        
                        
if __name__ == "__main__":
    sol = Solution()

    # input:
    arr = [0, 0, 2, 1, 1]
    target = 3
    # Output: [[0, 0, 1, 2]]

    print(sol.fourSum(arr, target))