class Solution:
    def countTriplets(self, n, sum, arr):
        #code here
        
        
        n = len(arr)
        arr.sort()
        count = 0
        
        for i in range(n):
            
            left = i+1
            right = n-1
            
            while left < right:
                arr_sum = arr[i] + arr[left] + arr[right]
                
                if arr_sum < sum:
                    count += (right-left)
                    left += 1
                else:
                    right -= 1
        
        # look if you simply do count +=1 then it will not give correct output. why?

        # in the below example: i=0, left=1, right=3 then its sum< target.  and we count it using count += 1. but then based on our cond^n left will move forward and then triplet (-2,0,1) will never be counted coz sum will be increasing at each step.  and i will never be 0 again. 
        
        # so did right-left . basically by dry run it come. 

        
        return count
    


if __name__ == "__main__":
    sol = Solution()

    # input:
    arr = [-2, 0, 1, 3]
    sum = 2
    n = len(arr)
    # Output: 2

    print(sol.countTriplets(n,sum,arr))