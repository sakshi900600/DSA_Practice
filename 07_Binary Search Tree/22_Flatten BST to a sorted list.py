
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def flattenBST(self, root):
        # code here
        li = []
        self.inorder(root, li)
        
        return self.createTree(li)
        
    
    def inorder(self, root, li):
        if root == None:
            return
        
        self.inorder(root.left, li)
        li.append(root.data)
        self.inorder(root.right, li)
        
    
    def createTree(self, li):
        dummy = Node(-1)
        temp = dummy
        
        for node in li:
            temp.right = Node(node)
            temp.left = None
            temp = temp.right
        
        return dummy.right
        
        

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    sol = Solution()
    newRoot = sol.flattenBST(root)
    
    while newRoot:
        print(newRoot.data, end=" ")
        newRoot = newRoot.right

    # output: 2 3 4 5 6 7 8 