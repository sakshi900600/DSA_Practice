#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        
        ans = []
        for i in range(len(arr)):
            if arr[i] == i+1:
                ans.append(arr[i])
                
                
        return ans
    


if __name__ == "__main__":
    sol = Solution()

    # input
    arr = [15, 2, 45, 4 , 7]
    # Output: [2, 4]

    print(sol.valueEqualToIndex(arr))
