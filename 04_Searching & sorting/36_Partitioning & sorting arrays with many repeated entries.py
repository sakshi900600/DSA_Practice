# This ques is same as 3-way partitioning where we have applied dutch national flag algorithm


#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
    def threeWayPartition(self, arr, a, b):
        # code here 
        n = len(arr)
        
        l=0
        m=0
        r=n-1
        
        while m <= r:
            if arr[m] <= a:
                arr[m],arr[l] = arr[l],arr[m]
                l += 1
                m += 1
            elif arr[m]>=a and arr[m]<=b:
                m += 1
            else:
                arr[m],arr[r] = arr[r],arr[m]
                r -= 1

        return arr
        
        

if __name__ == "__main__":
    sol = Solution()

    arr = [1, 4, 3, 6, 2, 1]
    a = 1
    b = 3

    print(sol.threeWayPartition(arr,a,b))

