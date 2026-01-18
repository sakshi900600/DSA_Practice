class Solution:
    def reverseFirstK(self, q, k):
        #code here 
        n = len(q)
        if k > n:
            return q
            
        st = []
        
        for i in range(k):
            st.append(q.popleft())
            
        
        while st:
            q.append(st.pop())
        
        
        for i in range(n-k):
            q.append(q.popleft())
        
        
        return q
        
        

if __name__ == "__main__":
    from collections import deque
    q = deque([1, 2, 3, 4, 5])
    k = 3
    sol = Solution()
    result = sol.reverseFirstK(q, k)
    print(list(result))  
    
    # Output: [3, 2, 1, 4, 5]