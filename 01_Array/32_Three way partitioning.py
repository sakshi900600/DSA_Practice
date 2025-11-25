# User function template for Python

class Solution:
    # Function to partition the array around the range such 
    # that array is divided into three parts.
    def threeWayPartition(self, arr, a, b):
        n = len(arr)
        
        l = 0
        m = 0
        r = n - 1
        
        while m <= r:
            if arr[m] < a:
                arr[m], arr[l] = arr[l], arr[m]
                l += 1
                m += 1
            elif a <= arr[m] <= b:
                m += 1
            else:
                arr[m], arr[r] = arr[r], arr[m]
                r -= 1






if __name__ == "__main__":
    sol = Solution()

    # Input: 
    arr = [1, 2, 3, 3, 4]
    a = 1
    b = 2
    # Output: true

    sol.threeWayPartition(arr,a,b)
    print(arr)