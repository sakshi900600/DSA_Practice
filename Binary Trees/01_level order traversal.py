"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""

from collections import deque
class Solution:
    def levelOrder(self, root):
        # code here
        
        if root == None:
            return
        
        ans = []
        q = deque()
        q.append(root)
        
        while q:
            
            size = len(q)
            temp = []
            
            for i in range(size):
                node = q.popleft()
                
                temp.append(node.data)
                
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                    
            ans.append(temp)
        
        return ans
        
        
        