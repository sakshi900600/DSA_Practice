
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def boundaryTraversal(self, root):
        # code here
        
        if root == None:
            return []
            
        ans = []
        if not self.isleaf(root):
            ans.append(root.data)
        
        self.leftBoundary(root.left,ans)
        self.addLeaf(root,ans)
        self.rightBoundary(root.right,ans)
        
        return ans
    
    
    def isleaf(self,root):
        return root.left == None and root.right == None
        
        
    
    def leftBoundary(self,root,ans):
        
        while root:
            if not self.isleaf(root):
                ans.append(root.data)
            
            
            if root.left != None:
                root = root.left
            else:
                root = root.right
                
                
    def rightBoundary(self,root,ans):
        temp = []
        while root:
            if not self.isleaf(root):
                temp.append(root.data)
            
            if root.right != None:
                root = root.right
            else:
                root = root.left
        
        temp.reverse()
        ans += temp
        
    
    def addLeaf(self,root,ans):
        if root == None:
            return
        
        if self.isleaf(root):
            ans.append(root.data)
            return
        
        self.addLeaf(root.left,ans)
        self.addLeaf(root.right,ans)
        
        
if __name__ == '__main__':

    # input:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    root.right.right.left = Node(10)
    root.right.right.right = Node(11)

    sol = Solution()
    # output:
    # [1, 2, 4, 8, 9, 6, 10, 11, 7, 3]
    
    print(sol.boundaryTraversal(root))