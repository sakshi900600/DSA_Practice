from collections import deque

class Solution:
    
    def check(self, root):
        #Code here
        if root == None:
            return True
            
        height = self.get_height(root)
        
        q = deque()
        q.append((root,0)) # node,level
        
        while q:
            node,level = q.popleft()
            
            if self.isleaf(node):
                if level != height:
                    return False
            
            if node.left != None:
                q.append((node.left, level+1))
            
            if node.right != None:
                q.append((node.right, level+1))
        
        
        return True
        
        
    def isleaf(self,root):
        return root.left == None and root.right == None
        
    
    def get_height(self,root):
        if root == None:
            return -1
        
        lh = self.get_height(root.left)
        rh = self.get_height(root.right)
        
        return 1 + max(lh,rh)


    # we are doing 2 traversals here
    # one for height and one for checking leaf levels

    # lets optimize it to single traversal
    def check_opt(self, root):
        #Code here
        if root == None:
            return True
        
        if self.isleaf(root):
            return True
            
        target_level = -1
        
        q = deque()
        q.append((root,0)) # node,level
        
        while q:
            node,level = q.popleft()
            

            if self.isleaf(node):
                if target_level == -1:
                    target_level = level
                elif level != target_level:
                    return False
            
            
            if node.left != None:
                q.append((node.left, level+1))
            
            if node.right != None:
                q.append((node.right, level+1))
        
        
        return True
        

        
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



if __name__ == "__main__":
    # input:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Output: True
    sol = Solution()
    # print(sol.check(root))
    print(sol.check_opt(root))