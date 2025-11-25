
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def reverseLevelOrder(self,root):
        # code here
        
        if root == None:
            return
        
        
        q = deque()
        st = []
        q.append(root)
        
        while  q:
            node = q.popleft()
            st.append(node.data)
            
            if node.right != None:
                q.append(node.right)
            
            if node.left != None:
                q.append(node.left)
                
                
        ans = []
        while st:
            ans.append(st.pop())
        
        return ans    
        
        
        
if __name__ == '__main__':

    # input:
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)

    sol = Solution()

    # output:
    # [2, 4, 3, 6, 5]
    
    print(sol.reverseLevelOrder(root))