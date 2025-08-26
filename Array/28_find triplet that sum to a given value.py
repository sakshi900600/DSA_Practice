class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        
        n = len(arr)
        arr.sort()
        
        for i in range(n):
            
            left = i+1
            right = n-1
            
            while left < right:
                sum = arr[i] + arr[left] + arr[right]
                
                if sum == target:
                    return True
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        
        return False
        


if __name__ == "__main__":
    sol = Solution()

    # Input: 
    arr = [1, 4, 45, 6, 10, 8]
    target = 13
    # Output: true 

    print(sol.hasTripletSum(arr,target))