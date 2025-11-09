#User function Template for python3

class Solution:
    def maximizeSum(self, a, n, k):
        # Your code goes here
        
        a.sort()
        
        # first do change neg to pos
        i = 0
        while k>0 and i<n and a[i] < 0:
            a[i] = -a[i]
            k -= 1
            i += 1
        
        
        # find total sum
        total = sum(a)
        min_elem = min(a)
        
        if k % 2 != 0:
            # in total sum min_elem was added so we need to remove that (sum - min_elem)
            # now coz we have one flip left. so we did min_elem = -min_elem. so we need to add it in sum
            
            # then newsum = oldsum - min_elem + (-min_elem)
            total -= 2 * min_elem
            
        
        return total
        
        
        
        
if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,-3,4,5]
    k = 1
    
    # Output: 15
    print(sol.maximizeSum(arr, len(arr), k))