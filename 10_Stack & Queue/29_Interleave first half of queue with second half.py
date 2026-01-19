from collections import deque
class Solution:
    def rearrangeQueue(self, q):
        #code here 
        
        first_half = deque()
        second_half = deque()
        half = len(q) // 2
        
        for i in range(half):
            first_half.append(q.popleft())
        
        while q:
            second_half.append(q.popleft())
        
        
        while first_half and second_half:
            q.append(first_half.popleft())
            q.append(second_half.popleft())
        
        
        return q



if __name__ == "__main__":
    q = deque([1, 2, 3, 4, 5, 6])
    solution = Solution()
    result = solution.rearrangeQueue(q)
    print(list(result))  
    # Output  [1, 4, 2, 5, 3, 6]