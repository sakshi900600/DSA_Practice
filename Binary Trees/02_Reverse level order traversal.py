'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

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
        
        
        
        