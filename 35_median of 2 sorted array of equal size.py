class Solution:
    def findMedian(self, arr):
        #code here.
        
        arr.sort()
        n = len(arr)
        
        if n % 2 != 0:
            return arr[n//2]
        else:
            e1 = arr[n//2]
            e2 = arr[n//2 -1]
            
            return (e1+e2)/2


if __name__ == "__main__":
    sol = Solution()


    arr = [90, 100, 78, 89, 67]
    # Output: 89

    print(sol.findMedian(arr))