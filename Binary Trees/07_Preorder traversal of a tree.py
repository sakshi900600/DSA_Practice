
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def preorder(self, root):
        # code here
        li = []
        self.helper(root,li)
        return li  
        
    def helper(self, root,li):
        # code here
        if root == None:
            return 

        li.append(root.data)
        self.helper(root.left,li)  
        self.helper(root.right,li)  

        
        