#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        n = len(arr)
        
        mod = 1000000007
        
        neg_count = 0
        zero_count = 0
        larg_neg = -9999 # -11 will work here based on constraints
        product = 1
        
        if n == 1:
            return arr[0]
        
        
        for i in range(n):
            if arr[i] == 0:
                zero_count += 1
                continue
            
            if arr[i] < 0:
                neg_count += 1
                larg_neg = max(larg_neg, arr[i])
            
            product *= arr[i]
        
        
        if zero_count == n:
            return 0
        
        if neg_count % 2 == 0:
            return product % mod
            
        else:
            
            # if there is 1 neg and all 0 value
            if neg_count==1 and zero_count > 0 and (zero_count + neg_count == n):
                return 0
            
            return (product//larg_neg) % mod
            
    

if __name__ == '__main__':
    
    # Input:
    arr = [-1, -1, -2, 4, 3]
    obj = Solution()

    # Output: 24
    print(obj.findMaxProduct(arr))