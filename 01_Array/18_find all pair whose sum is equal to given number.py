#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        
        arr.sort()
        n = len(arr)
        
        left = 0
        right = n-1
        
        ans = []
        
        while left < right:
            sum = arr[left] + arr[right]
            
            if sum == 0:
                
                ans.append((arr[left], arr[right]))
                left += 1
                right -= 1
            
            elif sum < 0 :
                left += 1
            else:
                right -= 1
                
        
        unique_pair = set(ans)
        
        final_ans = [list(pair) for pair in unique_pair]
        
        final_ans.sort()
        
        return final_ans
        
        
        
if __name__ == "__main__":
    sol = Solution()

    # input:
    arr = [-1, 0, 1, 2, -1, -4]

    # Output: [[-1, 1]]
    print(sol.getPairs(arr))