class Solution:
    def reverseQueue(self, q):
        # code here
        # 1. using stack
        # st = []
        # while q:
            # st.append(q.pop())
        
        # st.reverse()
        # print(st)
        
        # while st:
        #     q.append(st.pop())
        
        # return q
        
        
        # 2. using recursion
        if len(q)==0 or len(q) == 1:
            return 
    
        data = q[0]
        q.remove(q[0])
        
        self.reverseQueue(q)
        q.append(data)
        
        return q
        
        

if __name__ == "__main__":
    from collections import deque
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    q.append(5)

    sol = Solution()
    res = sol.reverseQueue(q)
    while res:
        print(res.popleft(), end=" ")
