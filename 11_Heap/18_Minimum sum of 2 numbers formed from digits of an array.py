class Solution:
    def minSum(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        
        l1 = []
        l2 = []
        
        for i in range(n):
            if i%2 == 0:
                l1.append(arr[i])
            else:
                l2.append(arr[i])
                
        
        return self.add_2_list(l1, l2)
        
        
        
    def add_2_list(self, l1, l2):
        n = len(l1)
        m = len(l2)
        
        i = n-1
        j = m-1
        carry = 0
        ans = []
        
        while i>=0 or j>=0 or carry>0:
            curr_sum = carry
            
            if i>=0:
                curr_sum += l1[i]
            if j>=0:
                curr_sum += l2[j]
            
            ans.append(str(curr_sum % 10))
            carry = curr_sum // 10
            
            i -= 1
            j -= 1
        
        
        # remove trailing 0 
        while ans and ans[-1] == '0':
            ans.pop()
        
        ans = ans[::-1]
        
        return "".join(ans)
        
            

if __name__ == "__main__":
    arr = [6, 8, 4, 5, 2, 3]
    sol = Solution()
    res = sol.minSum(arr)
    print(res)        
            
    # Output: 604
            
            
        