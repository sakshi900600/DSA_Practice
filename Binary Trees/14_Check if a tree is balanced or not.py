
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    # why added this:  self.isBalanced(root.left) and self.isBalanced(root.right)

    # coz above we only find out height of roots left subtree and roots right subtree and then check abs difference, (Only for root node)

    # but tree will be balanced when all nodes follow this thing. thats why calls the same fun for left and right subtree. 

    def isBalanced(self, root):
        # code here
        
        if root == None:
            return True
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        return abs(lh-rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def height(self,root):
        if root == None:
            return 0
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        return 1 + max(lh,rh)
        


if __name__ == '__main__':

    # input:
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)

    sol = Solution()
    # output:
    # True
    
    print(sol.isBalanced(root))