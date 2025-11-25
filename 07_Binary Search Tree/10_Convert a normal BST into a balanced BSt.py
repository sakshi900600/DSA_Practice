
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def balanceBST(self,root):
        #code here
        li = []
        self.inorder(root, li)
        
        return self.createBST(0,len(li)-1, li)
        
    
    def inorder(self, root, li):
        if root == None:
            return
        
        self.inorder(root.left, li)
        li.append(root.data)
        self.inorder(root.right, li)
    
    
    
    def createBST(self, si, ei, li):
        if si > ei:
            return None
            
        mid = (si+ei)//2
        root = Node(li[mid])
        
        root.left = self.createBST(si, mid-1, li)
        root.right = self.createBST(mid+1, ei, li)
        
        return root
        
    
    
    
if __name__ == "__main__":
    # input:
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)

    sol = Solution()
    new_root = sol.balanceBST(root)    
    print(new_root.data)  # Output: 20

    
    
    
    
        
        